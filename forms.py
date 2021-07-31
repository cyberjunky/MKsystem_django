from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, PasswordChangeForm
)
from django import forms
from .models import (
    User, Withdrawal, Asset, Image
)
import random
import string
from datetime import datetime

form_input_base_class = 'p-2 form-input block border w-100 mb-5 '
form_select_base_class = 'p-2 w-100  mb-5 '


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['picture']

    # def clean(self):
    #     cleaned_data = super().clean()


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': form_input_base_class,
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': form_input_base_class,
            }
        )
    )


class SignUpForm(UserCreationForm):
    required_css_class = 'required'

    user_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '8~16文字 半角英字、数字を使用できます。'}))
    zip = forms.CharField(label='郵便番号',
                          widget=forms.TextInput(attrs={'placeholder': '000-0000'}))
    phone = forms.CharField(label='電話番号',
                            widget=forms.TextInput(attrs={'placeholder': '000-0000-0000'}))

    class Meta:
        model = User
        fields = [
            'user_id',
            'rank',
            'family_name',
            'first_name',
            'zip',
            'address',
            'phone',
            'password1',
            'password2'
        ]

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name == "rank":
                visible.field.widget.attrs['class'] = form_select_base_class
            else:
                visible.field.widget.attrs['class'] = form_input_base_class

    def get_user_id(self):
        # usercount = User.objects.all().count()
        # ランダムな文字列を作る
        candidate_user_id = self.create_user_id(8)
        while self.check_already_user_id(candidate_user_id):
            candidate_user_id = self.create_user_id(8)

        return candidate_user_id

    def create_user_id(self, n):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))

    def check_already_user_id(self, candidate_user_id):
        list_user = [obj.user_id for obj in User.objects.all()]
        for user_id in list_user:
            if candidate_user_id == user_id:
                return True
        return False

    def clean_user_id(self):
        user_id = self.cleaned_data.get('user_id')
        if self.check_already_user_id(user_id):
            raise forms.ValidationError('既に使用されています。')
        return user_id

    # @override
    def save(self, commit=True):
        user = super().save(commit=False)
        # user.user_id = self.get_user_id()
        user.set_password(self.cleaned_data["password1"])
        # ランクの設定
        rank = user.rank
        if rank == 1:
            user.is_staff = True
            user.is_superuser = True
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    required_css_class = 'required'

    zip = forms.CharField(label='郵便番号',
                          widget=forms.TextInput(attrs={'placeholder': '000-0000'}))
    phone = forms.CharField(label='電話番号',
                            widget=forms.TextInput(attrs={'placeholder': '000-0000-0000'}))

    class Meta:
        model = User
        fields = (
            'zip',
            'address',
            'phone',
            'btc_address',
        )

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.required:
                visible.field.label = f'{visible.field.label}*'
            visible.field.widget.attrs['class'] = form_input_base_class


class PasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = form_input_base_class


class WithdrawalForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Withdrawal

        fields = (
            'value',
        )

    def __init__(self, *args, **kwargs):
        super(WithdrawalForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.required:
                visible.field.label = f'{visible.field.label}*'
            visible.field.widget.attrs['class'] = form_input_base_class

    def clean(self):
        cleaned_data = super().clean()
        value = cleaned_data.get("value")
        # MinValueValidatorでエラーが出せる
        # if value < 0.001:
        #     raise forms.ValidationError(
        #         "最小出金数量を下回ってます。"
        #     )
        # print(value)
        user_id = self.data["user_id"]
        # print(user_id)
        asset_objects = Asset.objects.all().filter(user_id=user_id).first()
        # print(asset_objects.asset)
        if asset_objects.asset < value:
            raise forms.ValidationError(
                "出金可能額以上は出金できません。"
            )


class AssetForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Asset

        fields = (
            "asset",
        )

    def __init__(self, *args, **kwargs):
        super(AssetForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.required:
                visible.field.label = f'{visible.field.label}*'
            visible.field.widget.attrs['class'] = form_input_base_class

    def clean(self):
        cleaned_data = super().clean()
        value = cleaned_data.get("asset")
        if value is not None:
            # print(value)
            user_id = self.data["user"]
            # print(user_id)
            user_objects = User.objects.all().filter(user_id=user_id)
            # print(user_objects[0].asset)
            if user_objects[0].asset < value:
                raise forms.ValidationError(
                    "出金可能額以下にして下さい。"
                )


class ShareRatioForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Asset
        fields = (
            "share_ratio",
        )

    def __init__(self, *args, **kwargs):
        super(ShareRatioForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.required:
                visible.field.label = f'{visible.field.label}*'
            visible.field.widget.attrs['class'] = form_input_base_class


class AcceptForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Asset

        fields = (
            'is_accept',
        )

    def __init__(self, *args, **kwargs):
        super(AcceptForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.required:
                visible.field.label = f'{visible.field.label}*'
            visible.field.widget.attrs['class'] = form_input_base_class
