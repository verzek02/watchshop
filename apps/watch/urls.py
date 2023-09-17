from django.urls import path, include
from rest_framework import routers, pagination, filters
from .views import WatchListCreateAPIView, WatchRetrieveUpdateDestroyAPIView

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10

class NameSearchFilter(filters.SearchFilter):
    search_param = 'name'

router = routers.DefaultRouter()
router.register('watches', WatchListCreateAPIView, basename='watch-list')
router.register('watches', WatchRetrieveUpdateDestroyAPIView, basename='watch-detail')
router.pagination_class = StandardResultsSetPagination
router.filter_backends = [NameSearchFilter]

urlpatterns = [
    path('', include(router.urls)),
]