from django.db import models


# Create your models here.
class BaseModel(models.Model):
    ctime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    mtime = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        # 定义抽象基类
        abstract = True


class Tag(BaseModel):
    name = models.CharField('标签名称', max_length=100)

    class Meta:
        ordering = ['-ctime']
        verbose_name_plural = verbose_name = '标签'

    def __str__(self):
        return self.name


class LinkResource(BaseModel):
    name = models.CharField(max_length=100, verbose_name='链接名称')
    url = models.CharField(max_length=255, verbose_name='链接地址')
    description = models.TextField(verbose_name='链接描述')
    tags = models.ManyToManyField(Tag, related_name='link_resources')
    owner = models.ForeignKey('auth.User',
                              related_name='link_resources',
                              null=True,
                              on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-ctime']
        verbose_name_plural = verbose_name = '链接资源'

    def __str__(self):
        return self.name
