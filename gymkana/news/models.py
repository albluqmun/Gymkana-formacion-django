from django.db import models
from django.db.models.fields.files import ImageField
from base.models import BaseItems
from django.core.exceptions import ValidationError
from django.core import validators
from .validators import image_size, image_extension

# Create your models here.

class New(BaseItems):

    publish_date = models.DateTimeField(auto_now_add=True)

    """
    validators only works on ModelForms. For objects validation, you need to use Model.clean_fields(), Model.clean(), Model.validate_unique() or Model.full_clean()
    https://docs.djangoproject.com/en/dev/ref/models/instances/#validating-objects
    """
    image = ImageField(default='default.jpg', validators=[image_size, image_extension])

    def clean(self):
        limit = 10 * 1024 * 1024
        if self.image.size > limit:
            raise ValidationError('The image should not exceed 10MB.')

        valid_extensions = ["jpg","png"]
        if not any([self.image.url.endswith(e) for e in valid_extensions]):
            raise ValidationError('The image must have a jpg or a png extension.')

    def __str__(self):
        return self.title

    