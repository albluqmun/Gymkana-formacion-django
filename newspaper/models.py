from django.db import models
from django.utils import timezone

# Create your models here.


class BaseItems(models.Model):
    title = models.CharField(blank=False, null=False, max_length=80)
    subtitle = models.CharField(blank=False, null=False, max_length=80)
    body = models.TextField(blank=False, null=False)

    class Meta:
        abstract = True


class New(BaseItems):
    publish_date = models.DateTimeField('date published', auto_now='True')
    image = models.ImageField(upload_to='', default='media/images/image.jpg')

    def __str__(self):
        return self.title + "This New was published the day {}.".format(self.publish_date)
      

class Event(BaseItems):
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.title + "This Event ends {}".format(self.end_date)
