from rest_framework.routers import DefaultRouter
from business_application.api.views import BusinessApplicationViewSet

router = DefaultRouter()
router.register(r'business-applications', BusinessApplicationViewSet, basename='businessapplication')

urlpatterns = router.urls
