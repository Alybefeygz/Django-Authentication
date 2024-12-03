from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    #Ek alanlar oluştur.
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    
    def __str__(self):
        return self.username