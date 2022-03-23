from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class BaseModel(models.Model):
    ctime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    mtime = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        # 定义抽象基类
        abstract = True


class Snippet(BaseModel):
    # created = models.DateTimeField(auto_now_add=True)
    title = models.CharField('标题', max_length=100, blank=True, default='')
    code = models.TextField('代码')
    linenos = models.BooleanField('显示行号', default=False)
    language = models.CharField('语言',
                                choices=LANGUAGE_CHOICES,
                                default='python',
                                max_length=100)
    style = models.CharField('风格',
                             choices=STYLE_CHOICES,
                             default='friendly',
                             max_length=100)
    owner = models.ForeignKey(
        'auth.User',
        related_name='snippets',
        null=True,
        on_delete=models.CASCADE,
        verbose_name='创建者',
    )
    highlighted = models.TextField('高亮显示', null=True)

    class Meta:
        ordering = ['-ctime']

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style,
                                  linenos=linenos,
                                  full=True,
                                  **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
