from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Farm(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    farm = models.CharField(max_length=50)
    total_areas = models.IntegerField()
    geo = models.CharField(max_length=50)
    total_plants = models.IntegerField()

