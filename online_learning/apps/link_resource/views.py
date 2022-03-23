from rest_framework import permissions
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination

from .models import LinkResource, Tag
from .permissions import IsOwnerOrReadOnly
from .serializers import LinkResourceSerializer, TagSerializer
from rest_framework import viewsets

# from django.contrib


# Create your views here.
class LargeResultsSetPagiation(PageNumberPagination):
    page_size = 2  # 默认每页显示多少条数据
    max_page_size = 5  # 前端在控制每页显示多少条时，最多不能超过 5
    page_query_param = 'page'  # 前端在查询字符串的关键字时指定显示第几页的名字，不指定默认为 page
    page_size_query_param = 'page_size'  # 前端在查询字符串的关键字名字，是用来控制每页显示多少条的关键字


class LinkResourceViewSet(viewsets.ModelViewSet):

    # 限流
    throttle_scope = 'link_resources'
    # 添加过滤字段
    filter_fields = {'name'}
    # 排序
    filter_backends = [OrderingFilter, SearchFilter]
    order_fields = {'id'}
    # 分页
    pagination_class = LargeResultsSetPagiation

    queryset = LinkResource.objects.all()
    serializer_class = LinkResourceSerializer

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
    ]

    # 关联用户
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TagsViewSet(viewsets.ModelViewSet):

    # 限流
    throttle_scope = 'tags'
    # 添加过滤字段
    filter_fields = {'name'}
    # 排序
    filter_backends = [OrderingFilter, SearchFilter]
    order_fields = {'id'}
    # 分页
    pagination_class = LargeResultsSetPagiation

    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
    ]
