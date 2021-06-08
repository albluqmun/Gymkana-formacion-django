import datetime

from django.urls import reverse
from django.utils import timezone
from django.test import TestCase

# Create your tests here.
from .models import New

def create_new(title, subtitle, body, days, image):
        publish_date = timezone.now() + datetime.timedelta(days = days)
        new = New(title=title, subtitle=subtitle,
        body=body,publish_date=publish_date,image=image)
        new.save()
        return new

class NewMethodTest(TestCase):

    """
    Index view tests
    """

    def test_no_news_function_view(self):
        response = self.client.get(reverse('news:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['news'],[])

    def test_no_news_class_view(self):
        response = self.client.get(reverse('news:index_view'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['news'],[])

    def test_one_new(self):
        create_new(title='Good new', subtitle='Subtitle', body='Body', 
        days=2, image='Gymkana-formacion-django/gymkana/media/default.jpg')
        response = self.client.get(reverse('news:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['news'],['<New: Good new>'])

    def test_one_bad_new(self):
        create_new(title='Bad new', subtitle='Subtitle', body='Body', 
        days=2, image='Gymkana-formacion-django/gymkana/media/yuhugasolina.gif')
        response = self.client.get(reverse('news:index'))
        self.assertQuerysetEqual(response.context['news'],[])

    def test_one_good_and_one_bad_new(self):
        create_new(title='Good new', subtitle='Subtitle', body='Body', 
        days=2, image='default.jpg')
        create_new(title='Bad new', subtitle='Subtitle', body='Body', 
        days=2, image='Gymkana-formacion-django/gymkana/media/yuhugasolina.gif')
        response = self.client.get(reverse('news:index'))
        self.assertQuerysetEqual(response.context['news'],['<New: Good new>'])

    def two_news(self):
        create_new(title='Good new 1', subtitle='Subtitle', body='Body', 
        days=2, image='default.jpg')
        create_new(title='Good new 2', subtitle='Subtitle', body='Body', 
        days=2, image='Gymkana-formacion-django/gymkana/media/default.jpg')
        response = self.client.get(reverse('news:index'))
        self.assertQuerysetEqual(response.context['news'],['<New: Good new 1>, <New: Good new 2>'])


    """
    Detail view tests
    """

    def test_good_new_displayed(self):
        good_new = create_new(title='Good new', subtitle='Subtitle', body='Body', 
        days=2, image='default.jpg')
        url = reverse('news:detail_view', kwargs={'pk': good_new.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_image_bad_mimetype(self):
        bad_new = create_new(title='Bad new', subtitle='Subtitle', body='Body', 
        days=2, image='yuhugasolina.gif')
        url = reverse('news:detail_view', kwargs={'pk': bad_new.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_image_bad_size(self):
        bad_new = create_new(title='Bad new', subtitle='Subtitle', body='Body', 
        days=2, image='Pano-bayer-leverkusen.jpg')
        url = reverse('news:detail_view', kwargs={'pk':bad_new.id,})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_new_no_title(self):
        bad_new = create_new(title='', subtitle='Subtitle', body='Body', 
        days=2, image='default.jpg')
        url = reverse('news:detail_view', kwargs={'pk': bad_new.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    """
    Update view tests
    """

    def test_new_updated(self):
        good_new = create_new(title='Good new', subtitle='Subtitle', body='Body', 
        days=2, image='default.jpg')
        client_response = self.client.post(reverse('news:update_view', kwargs={'pk':good_new.id}), 
        {'title':'Good new updated', 'subtitle':'Subtitle', 'body':'Body', 'days':'2021-10-12 21:20', 'image':'default.jpg'})
        good_new.refresh_from_db()
        self.assertRedirects(client_response, 'news:detail_view', kwargs={'pk': good_new.id})




