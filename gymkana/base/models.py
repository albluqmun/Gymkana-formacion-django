from django.db import models

# Create your models here.

class BaseItems(models.Model):
    title = models.CharField(max_length=100, blank=False)
    subtitle = models.CharField(max_length=100, blank=False)
    body = models.TextField(blank=False)

    class Meta:
        abstract = True
    
