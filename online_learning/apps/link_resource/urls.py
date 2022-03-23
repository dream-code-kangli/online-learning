from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'link-resources', views.LinkResourceViewSet, basename="link_resource")
router.register(r'tags', views.TagsViewSet, basename="tag")

# urlpatterns = [
#     path(r'api/', include(router.urls)),
#     # 查询所有和新增链接资源
#     path('', views.LinkResourcesView.as_view({'get': 'list'})),
#     # 查询、修改、删除某个链接资源
#     path('<int:pk>/', views.LinkResourceDetailView.as_view(), name='link-resource-detail'),
#     path('tags/', views.TagsView.as_view()),
#     path('tags/<int:pk>/', views.TagsDetailView.as_view()),
# ]
# # 可以使用 allowed=['json', 'html'] 参数指定允许的后缀
# urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns = [
    path('', include(router.urls)),
]
