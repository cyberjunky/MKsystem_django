from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import (
    UserChangeForm, UserCreationForm
)
from django.utils.translation import ugettext_lazy as _
from .models import User, Image


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('user_id', 'family_name', 'first_name', 'zip', 'address', 'phone',)


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('user_id', 'password')}),
        (_('Personal info'), {'fields': ('family_name', 'first_name', 'zip', 'address', 'phone')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        (_('Important dates'), {'fields': ('date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_id', 'family_name', 'first_name', 'zip', 'address', 'phone', 'password1', 'password2'),
        }),
    )
    form = MyUserChangeForm
    ordering = ('user_id',)
    add_form = MyUserCreationForm
    list_display = ('user_id', 'date_joined', 'family_name', 'first_name', 'zip', 'address', 'phone', 'is_superuser', 'is_staff')


admin.site.site_title = '管理'
admin.site.site_header = 'my admin '
admin.site.index_title = 'Menu'
admin.site.register(User, MyUserAdmin)
admin.site.register(Image)