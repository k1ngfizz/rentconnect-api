from rest_framework.permissions import BasePermission

class IsLandlordOfProperty(BasePermission):
    """
    Only the landlord who owns the property can update the booking status.
    """
    def has_object_permission(self, request, view, obj):
        return obj.property.landlord_id == request.user.id