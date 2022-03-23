from django.contrib import admin

from .models import LinkResource, Tag
from import_export.admin import ImportExportModelAdmin
from . import resource


class LinkResourceAdmin(ImportExportModelAdmin):
    resource_class = resource.LinkResource


# Register your models here.
admin.site.register(Tag)
admin.site.register(LinkResource, LinkResourceAdmin)
