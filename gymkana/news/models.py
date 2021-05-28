from django.db import models
from django.db.models.fields.files import ImageField
from base.models import BaseItems
from django.core import validators
from .validators import image_size, image_extension

# Create your models here.

class New(BaseItems):

    publish_date = models.DateTimeField(auto_now_add=True)
    image = ImageField(default='default.jpg', validators=[image_size, image_extension])

    class Meta(BaseItems.Meta):
        pass

    def __str__(self):
        return self.title