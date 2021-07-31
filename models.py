from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.core.validators import (
    RegexValidator, MaxValueValidator, MinValueValidator, MinLengthValidator
)
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class Image(models.Model):
    user_id = models.CharField(
        verbose_name='ユーザID',
        default="",
        max_length=10)
    picture = models.ImageField(upload_to='images/')
    date = models.DateTimeField(
        verbose_name='日時',
        null=True)

    def __str__(self):
        return self.picture


class Exchange(models.Model):
    """
        レート取得
        レートを取得してテーブルに保存する
    """
    rate = models.FloatField(
        verbose_name='',
        blank=True,
        null=True,
        default=0,
        validators=[
            # MinValueValidator(0.001),
        ],
    )
    date = models.DateTimeField(
        verbose_name='日時',
        null=True)


class Withdrawal(models.Model):
    """
        出金履歴
        管理者含めたすべての出金操作を取り扱う
    """
    # user = models.OneToOneField(settings.AUTH_USER_MODEL,
    #                             on_delete=models.CASCADE)
    user_id = models.CharField(verbose_name='ユーザID', max_length=10)
    date = models.DateTimeField(
        verbose_name='日時',
        null=True)
    value = models.FloatField(
        verbose_name='',
        blank=True,
        null=True,
        default=0,
        validators=[
            MinValueValidator(0.001),
            # RegexValidator(
            #     regex='\d{3}\-?\d{4}',
            #     message='フォーマットが不正です。',
            # )
        ],
    )

    # CHICE_STATUS = (
    #     (1, '処理中'),
    #     (2, '処理済'),
    # )
    # status = models.IntegerField(verbose_name='状況',
    #                            choices=CHICE_STATUS,
    #                            blank=True,
    #                            null=True,
    #                            default=1)

    status = models.CharField(
        verbose_name='状況',
        max_length=10,
        blank=True,
        null=True,
        default="処理中",
    )
    status_date = models.DateTimeField(
        verbose_name='変更日時',
        null=True)
    operate_user_id = models.CharField(
        verbose_name='操作したユーザID',
        max_length=10,
        blank=True,
        null=True,
    )


class Deposit(models.Model):
    """
        入金履歴
        入金操作を記録する
    """
    user_id = models.CharField(verbose_name='ユーザID', max_length=10)
    deposit_value = models.DecimalField(
        verbose_name='資産',
        max_digits=100,
        decimal_places=8,
        blank=True,
        null=True,
        default=0.00000000
    )
    deposit_date = models.DateTimeField(
        verbose_name='変更日時',
        null=True)
    operate_user_id = models.CharField(
        verbose_name='操作したユーザID',
        max_length=10,
        blank=True,
        null=True,
    )


class UserManager(BaseUserManager):
    error_css_class = 'error'
    """ユーザーマネージャー."""

    use_in_migrations = True

    def _create_user(self, user_id, password, **extra_fields):
        if not user_id:
            raise ValueError('The given user_id must be set')

        user = self.model(user_id=user_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, user_id, password=None, **extra_fields):
        """is_staff(管理サイトにログインできるか)と、is_superuer(全ての権限)をFalseに"""
        if extra_fields.get('rank') == 1:
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)
        else:
            extra_fields.setdefault('is_staff', False)
            extra_fields.setdefault('is_superuser', False)
        return self._create_user(user_id, password, **extra_fields)

    def create_superuser(self, user_id, password, **extra_fields):
        """スーパーユーザーは、is_staffとis_superuserをTrueに"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(user_id, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
        カスタムユーザ
    """

    def __str__(self):
        return self.user_id

    PERSON_RANK = (
        (1, '運営'),
        (2, '特別会員'),
        (3, '一般会員'),
    )

    user_id = models.CharField(
        verbose_name='ユーザID',
        max_length=16,
        primary_key=True,
        validators=[
            MinLengthValidator(8),
            RegexValidator(
                regex='^[0-9a-zA-Z]+$',
                message='フォーマットが不正です。'
            )
        ]
    )

    # rank = models.CharField(verbose_name='会員ランク', max_length=10)
    rank = models.IntegerField(
        verbose_name='会員ランク',
        choices=PERSON_RANK,
        blank=True,
        null=True,
        default=0)
    family_name = models.CharField(verbose_name='姓', max_length=50)
    first_name = models.CharField(verbose_name='名', max_length=50)
    zip = models.CharField(
        verbose_name='郵便番号',
        max_length=10,
        validators=[
            RegexValidator(
                regex='\d{3}\-?\d{4}',
                message='フォーマットが不正です。',
            )
        ]
    )
    address = models.CharField(verbose_name='住所', max_length=255)
    phone = models.CharField(
        verbose_name='電話番号',
        max_length=20,
        validators=[
            RegexValidator(
                # regex='[0-9\-\+]+',
                regex="(^0\d{9,10}$)|(^0\d{2,3}-\d{1,4}-\d{4}$)",
                message='フォーマットが不正です。'
            )
        ]
    )
    btc_address = models.CharField(
        verbose_name='ビットコインアドレス',
        default="",
        max_length=34,
        validators=[
            RegexValidator(
                regex='^[0-9a-zA-Z]+$',
                message='フォーマットが不正です。'
            )
        ]
    )
    date_joined = models.DateTimeField(verbose_name='登録日',
                                       default=timezone.now)
    is_staff = models.BooleanField(
        _('管理者'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('利用開始'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    # asset = models.DecimalField(
    #     verbose_name='資産',
    #     max_digits=100,
    #     decimal_places=8,
    #     blank=True,
    #     null=True,
    #     default=0.00000000
    # )
    USERNAME_FIELD = 'user_id'
    objects = UserManager()
    REQUIRED_FIELDS = [
        'rank',
        'family_name',
        'first_name',
        'zip',
        'address',
        'phone'
    ]


class Asset(models.Model):
    """
        ユーザごとの資産管理
        ユーザーを作るとassetテーブルができる
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    # asset = models.DecimalField(
    #     verbose_name='資産',
    #     max_digits=5,
    #     decimal_places=2,
    #     blank=True,
    #     null=True,
    #     default=0.00
    # )
    asset = models.FloatField(
        verbose_name='資産',
        blank=True,
        null=True,
        default=0,
        validators=[
            MinValueValidator(0.0001),
            # RegexValidator(
            #     regex='\d{3}\-?\d{4}',
            #     message='フォーマットが不正です。',
            # )
        ],
    )
    asset_date = models.DateTimeField(
        verbose_name='資産更新日付',
        null=True)
    is_accept = models.BooleanField(
        _('承諾'),
        default=False,
        # help_text=_(
        #     'Designates whether the user can log into this admin site.'),
    )
    accept_date = models.DateTimeField(
        verbose_name='承諾日付',
        null=True)
    stop_date = models.DateTimeField(
        verbose_name='運用停止日付',
        null=True)

    share_ratio = models.FloatField(
        verbose_name='配当比率',
        blank=True,
        null=True,
        default=0,
        validators=[
            MinValueValidator(0),
            # RegexValidator(
            #     regex='\d{3}\-?\d{4}',
            #     message='フォーマットが不正です。',
            # )
        ],
    )


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_asset(sender, instance, created, **kwargs):
    if created:
        Asset.objects.create(user=instance)

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_user_asset(sender, instance, **kwargs):
#     instance.asset.save()
