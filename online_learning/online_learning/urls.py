"""online_learning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

schema_view = get_schema_view(
    openapi.Info(
        title="在线学习平台API",
        default_version='v1.0',
        description="在线学习平台文档",
        terms_of_service="https://www.cnblogs.com/gooooodmorning/",
        contact=openapi.Contact(email="l_px@live.cn"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('link_resource.urls')),
    path('', include('snippets.urls')),
    path('', include('user.urls')),
    # api 添加登录功能
    path('api-auth/', include('rest_framework.urls')),
    # post 登录JWT，获取token的url
    path('api-token-auth/', obtain_jwt_token),
    # post 刷新JWT的token 的url
    path('api-token-refresh/', refresh_jwt_token),
    # 配置drf-yasg路由
    # swagger 文档
    re_path('^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    path('swagger/',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('docs/',
         schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-docs'),
    re_path(r'^auth/', include('rest_framework_social_oauth2.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
