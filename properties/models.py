from django.db import models
from users.models import User

class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ("house", "House"),
        ("apartment", "Apartment"),
        ("room", "Room"),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    available_from = models.DateField()
    image_url = models.URLField(blank=True, null=True)
    landlord = models.ForeignKey(User, related_name="properties", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.location})"
