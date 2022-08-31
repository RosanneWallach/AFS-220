from django.db import models

# Create your models here.

class Plan(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()
    details = models.TextField()
