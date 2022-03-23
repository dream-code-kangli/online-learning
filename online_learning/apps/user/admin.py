from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Profile
from .resource import ProfileResource


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )
    list_display = ('id', 'username', 'nickname', 'gender', 'avatar', 'phone',
                    'email', 'is_staff', 'is_active', 'is_superuser',
                    'address', 'job', 'company', 'description', 'last_login',
                    'date_joined')

    def nickname(self, obj):
        return obj.profile.nickname

    def gender(self, obj):
        return obj.profile.gender

    def avatar(self, obj):
        return obj.profile.avatar

    def phone(self, obj):
        return obj.profile.phone

    def address(self, obj):
        return obj.profile.address

    def job(self, obj):
        return obj.profile.job

    def company(self, obj):
        return obj.profile.company

    def description(self, obj):
        return obj.profile.description

    nickname.short_description = '昵称'
    gender.short_description = '性别'
    avatar.short_description = '头像'
    phone.short_description = '手机号'
    address.short_description = '所在地区'
    job.short_description = '职业'
    company.short_description = '公司/单位/学校'
    description.short_description = '个人简介'


# 重新注册 User 模型
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user', 'nickname', 'gender', 'avatar', 'address',
                    'job', 'company', 'description')
    # exclude = ('avatar',)
    resource_class = ProfileResource
