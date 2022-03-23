from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer


class LargeResultsSetPagiation(PageNumberPagination):
    page_size = 2  # 默认每页显示多少条数据
    max_page_size = 5  # 前端在控制每页显示多少条时，最多不能超过 5
    page_query_param = 'page'  # 前端在查询字符串的关键字时指定显示第几页的名字，不指定默认为 page
    page_size_query_param = 'page_size'  # 前端在查询字符串的关键字名字，是用来控制每页显示多少条的关键字


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # 限流
    throttle_scope = 'snippets'
    # 添加过滤字段
    filter_fields = {'title', 'code'}
    # 排序
    filter_backends = [OrderingFilter, SearchFilter]
    order_fields = {'id'}
    # 分页
    pagination_class = LargeResultsSetPagiation
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
    ]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
