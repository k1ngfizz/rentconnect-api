from rest_framework.routers import DefaultRouter
from .views import BookingRequestViewSet

router = DefaultRouter()
router.register(r'', BookingRequestViewSet, basename='booking')

urlpatterns = router.urls
