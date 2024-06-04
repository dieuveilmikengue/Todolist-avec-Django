from django.db import models
from datetime import date

# Create your models here.

class Taches(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now=True)