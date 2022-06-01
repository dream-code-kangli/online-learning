from django.db import models
from user.models import Profile

# Create your models here.

class Video(models.Model):
    ctime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    mtime = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    title = models.CharField(max_length=50, verbose_name='视频名称')
    path = models.CharField(max_length=150, verbose_name='视频路径')
    views = models.PositiveBigIntegerField(default=0, verbose_name='视频观看次数')
    praise_num = models.PositiveBigIntegerField(default=0, verbose_name='视频点赞数')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='视频作者', null=True)