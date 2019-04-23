from django.db import models
import datetime


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)
    DOB = models.DateField(default=None)
    FB = models.URLField(max_length=60)
    picture = models.ImageField()
    country = models.CharField(max_length=20)
    phone = models.CharField(max_length=11, default=None)

    def __str__(self):
        return self.first_name


