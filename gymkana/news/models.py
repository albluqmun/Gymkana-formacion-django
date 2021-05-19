from django.db import models

class BaseItem(models.Model):
    title = models.CharField(max_length=70)
    subtitle = models.CharField(max_length=100)
    body = models.TextField()

    class Meta:
        abstract = True
        ordering = ['title']

class New(BaseItem):
    publish_date = models.DateTimeField('date published', auto_now_add=True)
    image = models.ImageField(upload_to ='uploads/images/', default='default/static/news/images/default-news.jpeg')

    def __str__(self):
        return self.title