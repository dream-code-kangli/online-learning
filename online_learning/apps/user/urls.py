from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'profiles', views.ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
    path('send_mail_vcode/', views.send_mail_vcode, name='send_mail_vcode'),
    path('validate_mail_vcode/', views.validate_mail_vcode, name='validate_mail_vcode'),
]
