from django.db import models
from base.models import BaseItems

# Create your models here.
class Event(BaseItems):
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=False)

    class Meta(BaseItems.Meta):
        pass

    def __str__(self):
        return self.title