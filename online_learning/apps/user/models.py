from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.utils import timezone
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill
from datetime import date


# Create your models here.
class Profile(models.Model):
    GENDER_CHOICE = (
        ('0', '男'),
        ('1', '女'),
    )
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile')
    nickname = models.CharField('昵称',
                                max_length=20,
                                default=str(User.username))
    gender = models.CharField('性别', max_length=1, choices=GENDER_CHOICE)
    phone = models.CharField('手机号',
                             max_length=11,
                             unique=True,
                             default='11111111111')
    birthday = models.DateField('出生日期', default=date.today())
    avatar = ProcessedImageField(upload_to='imgs/avatar',
                                 processors=[ResizeToFill(90, 90)],
                                 format='JPEG',
                                 options={'quality': 300},
                                 verbose_name='头像',
                                 default='imgs/avatar/QQ图片20210912001251.jpg')
    address = models.CharField('所在地区',
                               max_length=20,
                               null=True,
                               blank=True,
                               help_text='省/市/区（县）')
    job = models.CharField('职业', max_length=20, null=True, blank=True)
    company = models.CharField('公司/单位/学校',
                               max_length=20,
                               null=True,
                               blank=True)
    description = models.CharField('个人简介',
                                   max_length=100,
                                   null=True,
                                   blank=True)

    class Meta:
        verbose_name_plural = verbose_name = '个人设置'

    def __str__(self):
        return f'<Profile: {self.nickname} for {self.user.username}>'
