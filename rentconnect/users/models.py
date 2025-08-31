from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # username, email, password, first_name, last_name already included
    is_landlord = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    