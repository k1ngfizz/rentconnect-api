from django.urls import path
from .views import BookingListCreateView, BookingStatusUpdateView

urlpatterns = [
    path("", BookingListCreateView.as_view(), name="booking-list-create"),
    path("<int:pk>/", BookingStatusUpdateView.as_view(), name="booking-status-update"),
]