import datetime

from django.core.urlresolvers import reverse
from django.utils import timezone
from django.test import TestCase

# Create your tests here.
from .models import New

def create_new(title, subtitle, body, days, image):
    publish_date = timezone.now() + datetime.timedelta(days = days)
    return New.objects.create(title=title, subtitle=subtitle,
    body=body,publish_date=publish_date,image=image)

class NewMethodTest(TestCase):

    """
    If there are no news, shows an message.

    #Preguntar a Ale o a Javi
    """
    def test_list_with_no_news(self):
        response = self.client.get(reverse('news:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No news are avaiable.")
        self.assertQuerysetEqual(response.context['news'],[])

    """
    News published in the future should not be displayed
    """
    def test_published_in_the_past(self):
        now = timezone.now()
        self.assertEqual()

    
    """
    TODO News published in the past should be displayed
    """

    """
    TODO News with no title, subtitle or body should not be displayed
    """

    """
    TODO News with an image that is not a jpg or png shoud not be displayed
    """





