from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

class BaseItems(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
  
    class Meta:
        abstract = True

class New(BaseItems):
    publish_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='', default='default.jpg', blank=True, validators=[FileExtensionValidator(['jpg', 'png'])])

    class Meta:
        ordering = ('-publish_date',)


class Event(BaseItems):
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        ordering = ('-start_date',)