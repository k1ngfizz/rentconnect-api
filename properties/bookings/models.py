from django.db import models
from users.models import User
from properties.models import Property

class BookingRequest(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("declined", "Declined"),
    ]
    user = models.ForeignKey(User, related_name="bookings", on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name="bookings", on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"Booking by {self.user.username} for {self.property.title}"
