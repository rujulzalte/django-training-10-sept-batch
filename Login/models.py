from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    age = models.IntegerField()
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    country = models.CharField(max_length=20)