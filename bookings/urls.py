from django.urls import path
from .views import BookingRequestCreateView, BookingRequestUpdateView

urlpatterns = [
    path("", BookingRequestCreateView.as_view(), name="booking-create"),
    path("<int:pk>/", BookingRequestUpdateView.as_view(), name="booking-update"),
]
