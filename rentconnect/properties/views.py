from rest_framework import generics, permissions, filters
from .models import Property
from .serializers import PropertySerializer
from .permissions import IsOwnerOrReadOnly
from .filters import PropertyFilter
from django_filters.rest_framework import DjangoFilterBackend

class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.filter(is_active=True)
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PropertyFilter
    search_fields = ["title", "description", "location"]
    ordering_fields = ["price", "created_at"]

    def perform_create(self, serializer):
        # Only landlords can create
        user = self.request.user
        if not user.is_authenticated or not user.is_landlord:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Only landlords can create properties.")
        serializer.save()

class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]