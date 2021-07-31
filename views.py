from datetime import datetime, timedelta

from django.shortcuts import (
    render, get_object_or_404
)
from django.shortcuts import (
    redirect
)
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView
)
from django.views.generic import (
    CreateView, UpdateView, TemplateView, ListView, DeleteView
)
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import (
    LoginForm, ProfileForm, SignUpForm, PasswordForm,
    WithdrawalForm, AssetForm, ShareRatioForm, AcceptForm, ImageForm
)
from .models import (
    User, Withdrawal, Asset, Image
)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.conf import settings
# User = settings.AUTH_USER_MODEL
# from django.http import HttpResponseRedirect

import MKsystemApp.lib.getBybit as getBybit
import MKsystemApp.lib.getDatabase as getDatabase
import MKsystemApp.lib.operateDatabase as operateDatabase
import MKsystemApp.lib.getBotStatus as getBotStatus


def showall(request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, 'MKsystemApp/test_image001.html', context)


# def image_upload(request):
#     if request.method == "POST":
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('MKsystemApp:test_image001')
#     else:
#         form = ImageForm()
# 
#     context = {'form': form}
#     return render(request, 'MKsystemApp/image_upload.html', context)


# class PostList(ListView):
#     context_object_name = 'post_list'
#     queryset = Post.objects.order_by('-created_date')
#     model = Post
#     paginate_by = 7
# 
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['tag_list'] = Tag.objects.all
#         return context


class OnlySuperuserMixin(UserPassesTestMixin):
    raise_exception = False  # set True if raise 403_Forbidden

    def test_func(self):
        user = self.request.user
        return user.is_superuser


class OnlyYouOrSuperuserMixin(UserPassesTestMixin):
    raise_exception = False  # set True if raise 403_Forbidden

    def test_func(self):
        user = self.request.user
        if 'pk' in self.kwargs:
            return user.pk == self.kwargs['pk'] or user.is_superuser
        else:
            return user.is_superuser


# Create your views here.
class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'MKsystemApp/login.html'


class Logout(LogoutView):
    pass


class Top(LoginRequiredMixin, TemplateView):
    model = Asset
    form_class = AcceptForm
    template_name = 'MKsystemApp/top.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Asset'] = Asset.objects.all().filter(user_id=self.request.user).first()
        return context

    # def get_success_url(self):
    #     return reverse_lazy('MKsystemApp:top',
    #                         kwargs={'pk': self.request.user.pk})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            asset_objects = Asset.objects.all().filter(user_id=self.request.user).first()
            is_accept = form.cleaned_data['is_accept']
            if is_accept:
                asset_objects.accept_date = datetime.now()  # + timedelta(hours=9)
                messages.success(self.request, '承諾しました。')
            else:
                asset_objects.stop_date = datetime.now()  # + timedelta(hours=9)
                messages.success(self.request, '運用停止しました。')
            asset_objects.is_accept = is_accept
            asset_objects.save()
            return redirect(to="MKsystemApp:top")


class Chart(LoginRequiredMixin, TemplateView):
    template_name = 'MKsystemApp/test_chart003.html'


class Countup(LoginRequiredMixin, TemplateView):
    template_name = 'MKsystemApp/test_countup002.html'


class WithdrawalRequest(OnlyYouOrSuperuserMixin, CreateView):
    """
        出金依頼ページ用
    """
    model = Withdrawal
    form_class = WithdrawalForm
    template_name = 'MKsystemApp/withdrawal_request.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Asset'] = Asset.objects.all().filter(user_id=self.request.user).first()
        return context

    def get_success_url(self):
        return reverse_lazy('MKsystemApp:withdrawal_request',
                            kwargs={'pk': self.request.user.pk})

    # def form_invalid(self, form):
    # messages.add_message(self.request, messages.WARNING, form.errors)
    # return super().form_invalid(form)

    # def form_valid(self, form):
    def form_valid(self, form, **kwargs):
        # messages.add_message(self.request, messages.WARNING, form.errors)
        # return super().form_invalid(form)
        # 資産を取り出す
        asset_objects = Asset.objects.all().filter(user_id=self.request.user).first()
        asset = asset_objects.asset
        # print(asset)
        value = form.cleaned_data['value']
        # print(value)
        post = form.save(commit=False)
        post.user_id = self.request.user
        post.date = datetime.now()  # + timedelta(hours=9)
        post.status_date = datetime.now()  # + timedelta(hours=9)
        post.save()
        asset_objects.asset = float(asset) - value
        asset_objects.save()
        messages.success(self.request, '出金依頼しました。')
        return redirect('MKsystemApp:withdrawal_request', self.request.user.pk)
        # return ret


class WithdrawalList(OnlySuperuserMixin, ListView):
    """
        出金依頼一覧ページ用
    """
    model = Withdrawal
    template_name = 'MKsystemApp/list_withdrawal.html'
    queryset = Withdrawal.objects.all().order_by('pk')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['user_list'] = User.objects.all
        return context


class WithdrawalHistory(OnlyYouOrSuperuserMixin, ListView):
    """
        出金履歴ページ用
    """
    model = Withdrawal
    template_name = 'MKsystemApp/withdrawal_history.html'

    # queryset = Withdrawal.objects.filter(age='23')
    # queryset = Withdrawal.objects.all().order_by('pk')

    # paginationを入れるときは以下を入れれば良い
    # paginate_by = 5

    # user情報を取得するには以下のようにする
    # WithdrawalListではobjects.all()にすればよい

    def get_queryset(self):
        return Withdrawal.objects.filter(user_id=self.request.user).order_by('pk')

    # def get(self, request, *args, **kwargs):
    #     print(request.user)
    #     
    #     return super().get(request, **kwargs)


class Deposit(OnlySuperuserMixin, ListView):
    model = Asset
    template_name = 'MKsystemApp/list_deposit.html'
    queryset = User.objects.all().order_by('pk')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['asset_list'] = Asset.objects.all().order_by('pk')
        return context

    # def get(self, request, *args, **kwargs):
    #     # print(request.user)
    #     return super().get(request, *args, **kwargs)

    # def get_success_url(self):
    #     return reverse_lazy('MKsystemApp:deposit',
    #                         kwargs={'pk': self.request.user.pk})

class ShareRatio(OnlySuperuserMixin, ListView):
    model = Asset
    form_class = ShareRatioForm
    template_name = 'MKsystemApp/list_shareratio.html'
    queryset = User.objects.all().order_by('pk')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['asset_list'] = Asset.objects.all().order_by('pk')
        return context

    # def get(self, request, *args, **kwargs):
    #     # print(request.user)
    #     return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        # print(form.data["share_ratio"])
        user_id = form.data["user_id"]
        # user_id = user.data
        if form.is_valid():
            asset_objects = Asset.objects.all().filter(user_id=user_id).first()
            asset_objects.share_ratio = float(form.data["share_ratio"])
            asset_objects.save()
            messages.success(self.request, '更新しました。')
        return redirect("MKsystemApp:list_shareratio")
    
    # def get_success_url(self):
    #     return reverse_lazy('MKsystemApp:list_shareratio',
    #                         kwargs={'pk': self.request.user.pk})


def paginate_queryset(request, queryset, count):
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj


class Profile(OnlyYouOrSuperuserMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'MKsystemApp/profile.html'

    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        ret['user'] = self.request.user
        return ret

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['Image'] = Image.objects.all().filter(user_id=self.request.user).first()
    #     context['user'] = self.request.user
    #     return context

    def get(self, request, *args, **kwargs):
        # print(request.user)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form, **kwargs):
        # 上手くいかない
        for field in form.errors:
            form[field].field.widget.attrs['class'] += ' text-danger'
        ret = super().form_valid(form, **kwargs)
        messages.success(self.request, '更新しました。')
        return ret

    def get_success_url(self):
        return reverse_lazy('MKsystemApp:profile', kwargs={'pk': self.kwargs['pk']})


class ImageUpload(OnlyYouOrSuperuserMixin, CreateView):
    model = Image
    form_class = ImageForm
    template_name = 'MKsystemApp/image_upload.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['user'] = self.request.user
        images = Image.objects.filter(user_id=self.request.user).all()
        for image in images:
            print(image.picture)
        print(len(images))
        context['image_count'] = len(images)
        return context
    
    def post(self, request, *args, **kwargs):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = Image()
            image.user_id = self.request.user
            image.picture = form.cleaned_data["picture"]
            image.date = datetime.now()
            image.save()
            messages.success(self.request, 'アップロードしました。')
            return redirect('MKsystemApp:image_upload', self.request.user.pk)

    # def get_success_url(self):
    #     return reverse_lazy('MKsystemApp:image_upload', kwargs={'pk': self.kwargs['pk']})


class SignUp(OnlySuperuserMixin, CreateView):
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy('MKsystemApp:login')
    template_name = 'MKsystemApp/signup.html'

    def form_valid(self, form):
        ret = super().form_valid(form)
        messages.success(self.request, f'ユーザ:{self.object.user_id} 登録完了しました。')
        return ret


class ChangePassword(OnlyYouOrSuperuserMixin, PasswordChangeView):
    template_name = 'MKsystemApp/change_password.html'
    form_class = PasswordForm

    def get_success_url(self):
        messages.success(self.request, 'パスワードを更新しました')
        return reverse_lazy('MKsystemApp:profile', kwargs={'pk': self.request.user.pk})


class ListUser(OnlySuperuserMixin, ListView):
    model = User
    template_name = 'MKsystemApp/list_user.html'
    queryset = User.objects.all().order_by('pk')


def GetBalance(request):
    bot_no = request.POST.get("bot_no")
    return getBybit.get_balance(bot_no)


def GetUSDrate(request):
    return getBybit.get_usdrate()


def ReadExchange(request):
    return operateDatabase.read_exchange()


def GetAssetData(request):
    # 資産を取り出す
    asset_objects = Asset.objects.all().filter(user_id=request.user.user_id).first()
    asset = asset_objects.asset
    return getDatabase.get_assetdata(request.user.user_id, asset)


def GetBotStatus(request):
    # Botの状況を取得する
    return getBotStatus.get_botstatus()


def GetProfitData(request):
    return getDatabase.get_profitdata()


class DeleteUser(OnlySuperuserMixin, DeleteView):
    model = User
    template_name = 'MKsystemApp/delete_user.html'
    success_url = reverse_lazy('MKsystemApp:list_user')

    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        ret['user'] = self.request.user
        return ret


def change_status(request):
    operate_user_id = request.user.user_id
    id = request.POST.get("id")
    status_val = request.POST.get("sel_value")
    str_status = get_status(status_val)

    # s = Withdrawal.objects.filter(id=id).first()
    # s.status = get_status(status_val)
    # s.status_date = datetime.now()
    # s.operate_user_id = user_id
    # s.save()
    return operateDatabase.change_status(id, str_status, operate_user_id)
    # return redirect('MKsystemApp:list_withdrawal', request.user.pk)


def change_deposit(request):
    # print(request.POST.get("id"))
    # print(request.POST.get("sel_value"))
    user_id = request.POST.get("user_id")
    deposit_value = float(request.POST.get("deposit_value"))
    operate_user_id = request.user.user_id
    return operateDatabase.change_deposit(user_id, deposit_value, operate_user_id)


def get_status(status_val):
    if status_val == "sel-1":
        return "処理中"
    if status_val == "sel-2":
        return "処理済"
    return ""
