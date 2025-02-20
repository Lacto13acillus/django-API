

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User (models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        self.username

    


