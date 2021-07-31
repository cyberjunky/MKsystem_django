from django.urls import path, include
from MKsystemApp import views

app_name = 'MKsystemApp'
urlpatterns = [
    path('test_image001/', views.showall, name='test_image001'),
    # path('image_upload/', views.image_upload, name='image_upload'),
    path('', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('top/', views.Top.as_view(), name='top'),
    path('top/get_usdrate', views.GetUSDrate),
    path('top/read_exchange', views.ReadExchange),
    path('top/get_balance', views.GetBalance),
    path('top/get_assetdata', views.GetAssetData),
    path('top/get_botstatus', views.GetBotStatus),
    path('chart/', views.Chart.as_view(), name='chart'),
    path('chart/get_profitdata', views.GetProfitData),
    path('countup/', views.Countup.as_view(), name='countup'),
    path('signup/', views.SignUp.as_view(), name='add_user'),
    path('users/', views.ListUser.as_view(), name='list_user'),
    path('list_withdrawal/', views.WithdrawalList.as_view(), name='list_withdrawal'),
    path("list_withdrawal/changestatus", views.change_status),
    path('deposit/', views.Deposit.as_view(), name='list_deposit'),
    path('deposit/changedeposit', views.change_deposit),
    path('list_shareratio/', views.ShareRatio.as_view(), name='list_shareratio'),
    path('users/<str:pk>/profile', views.Profile.as_view(), name='profile'),
    path('users/<str:pk>/image_upload', views.ImageUpload.as_view(), name='image_upload'),
    path('users/<str:pk>/withdrawal_request', views.WithdrawalRequest.as_view(), name='withdrawal_request'),
    path('users/<str:pk>/withdrawal_history', views.WithdrawalHistory.as_view(), name='withdrawal_history'),
    path('users/<str:pk>/delete', views.DeleteUser.as_view(), name='delete_user'),
    path('users/<str:pk>/change-password', views.ChangePassword.as_view(), name='change_password'),
]
