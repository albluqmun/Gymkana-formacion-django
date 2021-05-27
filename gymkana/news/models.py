from django.db import models
from django.db.models.fields.files import ImageField
from base.models import BaseItems

# Create your models here.

class New(BaseItems):

    publish_date = models.DateTimeField(auto_now_add=True)
    image = ImageField(default='default.jpg')

    class Meta(BaseItems.Meta):
        pass

    def __str__(self):
        return self.title