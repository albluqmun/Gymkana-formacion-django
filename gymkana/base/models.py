from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.

class BaseItems(models.Model):
    title = models.CharField(max_length=100, blank=False)
    subtitle = models.CharField(max_length=100, blank=False)
    body = models.TextField(blank=False)

    class Meta:
        abstract = True


class Event(BaseItems):
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=False)

    class Meta(BaseItems.Meta):
        pass

    def __str__(self):
        return self.title


class New(BaseItems):

    """
    TODO Default image

    def default_image():
        return image
    """
    publish_date = models.DateTimeField(auto_now_add=True)
    image = ImageField()

    class Meta(BaseItems.Meta):
        pass

    def __str__(self):
        return self.title
    
