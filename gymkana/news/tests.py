import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import New

def create_new(new_title, days):
    """
    Create a question with the given `new_title` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    subtitle = 'Testing'
    body = 'Some text here...'
    return New.objects.create(title=new_title, subtitle=subtitle, body=body, publish_date=time)

# Create your tests here.
class NewModelTests(TestCase):
    def test_no_news(self):
        """
        If no news exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('news:index-1'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No news are available.")
        self.assertQuerysetEqual(response.context['latest_news_list'], [])

    def test_past_new(self):
        """
        News with a publish_date in the past are displayed on the
        index page.
        """
        create_new(new_title="Past new.", days=-30)
        response = self.client.get(reverse('news:index-1'))
        self.assertQuerysetEqual(
            response.context['latest_news_list'],
            ['<New: Past new.>']
        )

    def test_future_new(self):
        """
        News with a publish_date in the future aren't displayed on
        the index page.
        """
        create_new(new_title="Future new.", days=30)
        response = self.client.get(reverse('news:index-1'))
        self.assertContains(response, "No news are available.")
        self.assertQuerysetEqual(response.context['latest_news_list'], [])

    def test_future_new_and_past_new(self):
        """
        Even if both past and future news exist, only past news
        are displayed.
        """
        create_new(new_title="Past new.", days=-30)
        create_new(new_title="Future new.", days=30)
        response = self.client.get(reverse('news:index-1'))
        self.assertQuerysetEqual(
            response.context['latest_news_list'],
            ['<New: Past new.>']
        )