from rest_framework import serializers
from .models import BookingRequest

class BookingRequestSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source="user.username", read_only=True)
    property_title = serializers.CharField(source="property.title", read_only=True)

    class Meta:
        model = BookingRequest
        fields = ["id","user","user_username","property","property_title","message","status","created_at"]
        read_only_fields = ["user","status","created_at"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)