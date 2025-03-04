from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=32, unique=True)
    email = models.EmailField(max_length=32, unique=True)
    password = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.username}"