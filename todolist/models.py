from django.db import models

# Create your models here.

class Taches(models.Model):
    title = models.CharField(max_length=70)