from django.db import models
from django.utils import timezone

# Create your models here.


class BaseItems(models.Model):
    title = models.CharField(max_length=80)
    subtitle = models.CharField(max_length=80)
    body = models.CharField(max_length=None)
    
    class Meta:
        abstract = True
            


class New(models.Model):
   publish_date = models.DateTimeField('date published', auto_now='True')
   image = models.ImageField(upload_to='media/images/', default='media/images/image.jpg')


class Event(models.Model):
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
