from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import BookingRequest
from .serializers import BookingRequestSerializer
from .permissions import IsLandlordOfProperty

class BookingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingRequestSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return BookingRequest.objects.none()
        # Tenants see their own bookings; landlords see requests on their properties
        if user.is_landlord:
            return BookingRequest.objects.filter(property__landlord=user)
        return BookingRequest.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        if not user.is_authenticated or user.is_landlord:
            raise PermissionDenied("Only tenants can create booking requests.")
        serializer.save()

class BookingStatusUpdateView(generics.UpdateAPIView):
    queryset = BookingRequest.objects.all()
    serializer_class = BookingRequestSerializer
    permission_classes = [permissions.IsAuthenticated, IsLandlordOfProperty]

    def perform_update(self, serializer):
        # Landlord can set status to accepted/declined
        serializer.save()