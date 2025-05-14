from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api.views import BusinessApplicationViewSet, DeviceDownstreamAppsViewSet, ClusterDownstreamAppsViewSet

router = DefaultRouter()
router.register(r'business-applications', BusinessApplicationViewSet)
router.register(r'devices', DeviceDownstreamAppsViewSet, basename='device-downstream-apps')
router.register(r'clusters', ClusterDownstreamAppsViewSet, basename='cluster-downstream-apps')

urlpatterns = router.urls + [
    path(
        'devices/downstream-applications/<int:pk>/',
        DeviceDownstreamAppsViewSet.as_view({'get': 'retrieve'}),
        name='device-downstream-applications-detail'
    ),
    path(
        'devices/downstream-applications/',
        DeviceDownstreamAppsViewSet.as_view({'get': 'list'}),
        name='device-downstream-applications-list'
    ),
    path(
        'clusters/downstream-applications/<int:pk>/',
        ClusterDownstreamAppsViewSet.as_view({'get': 'retrieve'}),
        name='cluster-downstream-applications-detail'
    ),
]
