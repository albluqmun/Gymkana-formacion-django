import datetime

from django.urls import reverse
from django.utils import timezone
from django.test import TestCase

# Create your tests here.
from .models import New

class NewMethodTest(TestCase):

    def create_new(title, subtitle, body, days, image):
        publish_date = timezone.now() + datetime.timedelta(days = days)
        return New.objects.create(title=title, subtitle=subtitle,
        body=body,publish_date=publish_date,image=image)

    def setUp(self):                                                                                                                                                                                                                                                                                                                                            j                                                          )

    """
    If there are no news, shows an message.

    """
    def test_list_with_no_news(self):
        response = self.client.get(reverse('news:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No news are avaiable.")
        self.assertQuerysetEqual(response.context['news'],[])

    """
    News published in the future should not be displayed
    """
    
    """
    TODO News published in the past should be displayed
    """

    """
    TODO News with no title, subtitle or body should not be displayed
    """

    """
    TODO News with an image that is not a jpg or png shoud not be displayed
    """





