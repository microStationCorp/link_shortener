from django.db import models

# Create your models here.

class SlugTable(models.Model):
    slug=models.CharField(max_length=100)
    url=models.CharField(max_length=400)