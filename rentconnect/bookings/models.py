from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from properties.models import Property

class BookingRequest(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("declined", "Declined"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="booking_requests")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="booking_requests")
    message = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ("user", "property")  # prevent duplicate interest by same user

    def __str__(self):
        return f"{self.user} -> {self.property} ({self.status})"