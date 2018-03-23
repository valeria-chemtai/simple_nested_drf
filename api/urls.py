from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import NestedRouterMixin

from api.views import AuthorViewSet, BookViewSet


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()

authors_router = router.register('authors', AuthorViewSet, base_name='author')

authors_router.register('books', BookViewSet, base_name='author-books',
                        parents_query_lookups=['author'])
