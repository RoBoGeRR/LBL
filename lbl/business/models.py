from unicodedata import category
from django.db import models

# Create your models here.
from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
    latitude = models.FloatField()
    longtitude = models.FloatField()

    def __str__(self):
        return self.name
