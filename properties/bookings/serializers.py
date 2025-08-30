from rest_framework import serializers
from .models import BookingRequest

class BookingRequestSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    property = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = BookingRequest
        fields = "__all__"
        read_only_fields = ["user", "status"]
