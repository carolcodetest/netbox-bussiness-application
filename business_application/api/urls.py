from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api.views import BusinessApplicationViewSet, DeviceDownstreamAppsViewSet, ClusterDownstreamAppsViewSet

router = DefaultRouter()
router.register(r'business-applications', BusinessApplicationViewSet)
router.register(r'devices', DeviceDownstreamAppsViewSet, basename='device-downstream-apps')
router.register(r'clusters', ClusterDownstreamAppsViewSet, basename='cluster-downstream-apps')

urlpatterns = [
    path('', include(router.urls)),
]
