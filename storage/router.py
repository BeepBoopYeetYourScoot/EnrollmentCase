from rest_framework.routers import DefaultRouter

from storage.views import StorageViewSet, total_cost

router = DefaultRouter()

router.register('', StorageViewSet)
