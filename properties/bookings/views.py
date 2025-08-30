from rest_framework import generics, permissions
from .models import BookingRequest
from .serializers import BookingRequestSerializer
from properties.models import Property

class IsTenant(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and not request.user.is_landlord

class IsLandlordForBooking(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Only the property owner can update status
        return obj.property.landlord == request.user

class BookingRequestCreateView(generics.CreateAPIView):
    queryset = BookingRequest.objects.all()
    serializer_class = BookingRequestSerializer
    permission_classes = [IsTenant]

    def perform_create(self, serializer):
        property_id = self.request.data.get("property_id")
        try:
            prop = Property.objects.get(id=property_id)
        except Property.DoesNotExist:
            raise serializers.ValidationError("Invalid property.")
        serializer.save(user=self.request.user, property=prop)

class BookingRequestUpdateView(generics.UpdateAPIView):
    queryset = BookingRequest.objects.all()
    serializer_class = BookingRequestSerializer
    permission_classes = [IsLandlordForBooking]
    http_method_names = ["patch"]
