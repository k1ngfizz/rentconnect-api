import django_filters
from .models import Property

class PropertyFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    bedrooms = django_filters.NumberFilter(field_name="bedrooms", lookup_expr="gte")
    bathrooms = django_filters.NumberFilter(field_name="bathrooms", lookup_expr="gte")

    class Meta:
        model = Property
        fields = ["location", "property_type", "min_price", "max_price", "bedrooms", "bathrooms"]