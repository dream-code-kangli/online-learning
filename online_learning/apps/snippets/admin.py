from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Snippet
from .resource import SnippetResource


# Register your models here.
@admin.register(Snippet)
class SnippetAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'language', 'code', 'style', 'owner')
    ordering = ['id']
    # 空值默认显示
    empty_value_display = 'null'
    resource_class = SnippetResource
