from import_export import resources
from .models import Profile


class ProfileResource(resources.ModelResource):

    class Meta:
        model = Profile
        # 导入排除字段
        exclude = ['id']
        # 设置主键字段导入更新数据
        import_id_fields = ['nickname']
