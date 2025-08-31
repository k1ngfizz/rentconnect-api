from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    landlord_username = serializers.CharField(source="landlord.username", read_only=True)

    class Meta:
        model = Property
        fields = [
            "id","title","description","location","price","property_type",
            "bedrooms","bathrooms","available_from","image_url","landlord",
            "landlord_username","is_active","created_at"
        ]
        read_only_fields = ["landlord","is_active","created_at"]

    def create(self, validated_data):
        validated_data["landlord"] = self.context["request"].user
        return super().create(validated_data)