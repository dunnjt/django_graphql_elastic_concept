from django.db import models

# Create your models here.
class CoreMetrics(models.Model):
    data = models.TextField(blank=True)