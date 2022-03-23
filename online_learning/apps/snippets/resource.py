from import_export import resources
from .models import Snippet


class SnippetResource(resources.ModelResource):

    class Meta:
        model = Snippet
        # 导入排除字段
        exclude = ['id']
        # 设置主键字段导入更新数据
        import_id_fields = ['title']
