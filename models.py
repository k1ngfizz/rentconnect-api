from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_landlord = models.BooleanField(default=False)
    # By default, is_tenant = not is_landlord (not stored, just logical)
    
    def __str__(self):
        return self.username
