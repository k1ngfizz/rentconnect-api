from rest_framework import generics, permissions, filters
from .models import Property
from .serializers import PropertySerializer

class IsLandlord(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_landlord

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Landlord can update/delete their own
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.landlord == request.user

class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["location", "property_type"]
    ordering_fields = ["price", "available_from"]

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsLandlord()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(landlord=self.request.user)

class PropertyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsOwnerOrReadOnly]
