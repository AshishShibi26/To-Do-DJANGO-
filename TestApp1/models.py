from django.db import models

# Create your models here.
class task(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()