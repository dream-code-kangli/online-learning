import time

from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import viewsets

from .mail_helper import send_vcode
from .models import Profile
from .serializers import ProfileSerializer, UserSerializer
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['POST'])
def send_mail_vcode(request):
    username = request.data.get('username')

    # 获取上次发送邮件的时间
    mail_vcode_time = request.session.get('mail_vcode_time')
    now_time = time.time()

    if mail_vcode_time and now_time < mail_vcode_time + settings.MAIL_INTERVAL:
        return JsonResponse({'msg': f'{settings.MAIL_INTERVAL}秒之内，不能重复发送邮件'})
    else:
        vcode = send_vcode(settings.MAIL_SMTP_SERVER, settings.MAIL_FROM_ADDR,
                           settings.MAIL_PASSWORD, username)

        # 存储验证码
        request.session['mail'] = username
        # 存储发送邮箱
        request.session['mail_vcode'] = vcode
        # 存储发送邮件时间
        request.session['mail_vcode_time'] = time.time()

        return Response({'msg': '您的验证码已经发送，请查阅邮箱'})


@api_view(['POST'])
def validate_mail_vcode(request):
    session_username = request.session.get('mail')
    username = request.data.get('username')

    if session_username and session_username == username:
        now_time = time.time()
        vcode_time = request.session.get('mail_vcode_time')

        if vcode_time and now_time <= vcode_time + settings.VCODE_EXPIRE:
            vcode = request.data.get('vcode')
            mail_vcode = request.session.get('mail_vcode')

            if mail_vcode and mail_vcode == vcode:
                resp = {'ok': 1, 'msg': '验证码验证正确！'}
            else:
                resp = {'ok': 0, 'msg': '验证码错误！'}
        else:
            resp = {'ok': 0, 'msg': '验证码已经过期，请重新获取！'}
    else:
        resp = {'ok': 0, 'msg': '该邮箱还没有获取验证码！'}

    return Response(resp)
