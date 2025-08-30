from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    landlord = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Property
        fields = "__all__"
        read_only_fields = ["landlord"]
