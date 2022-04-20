from django.test import TestCase
from .models import New, Event
from django.conf.urls.static import static
from django.conf import settings
from django.test import Client
from django.urls import reverse, reverse_lazy
# Create your tests here.

class TestUrls(TestCase):
    
    def test_setting_debug_false(self):
        self.assertFalse(settings.DEBUG)

class TestModel(TestCase):

    def setUp(self):
        self.news = New.objects.create(title='title', subtitle = "subtitle", body='body')

    def test_news_str(self):
        self.assertEqual(self.news.__str__(), 'title')
    
        
class TestView(TestCase):

    def setUp(self):
        return New.objects.create(title='title', subtitle="subtitle",  body='body', image='image')

    def test_index_get_list_news(self):
        response = self.client.get('/')
        #Fixme: error 404
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')
        self.assertContains(response, 'title')
        self.assertContains(response, 'body')
        self.assertContains(response, 'image')
    
    def test_index_get_event(self):
        response = self.client.get(reverse_lazy('index'))
        #Fixme: error 404
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')
        self.assertContains(response, 'start_date')
        self.assertContains(response, 'end_date')

    def test_list_news_get(self):
        
        url = reverse_lazy('list_news')
        resp = self.client.get(url, follow=True)

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'core/list_news.html')
        self.assertContains(resp, 'title')
        self.assertContains(resp, 'subtitle')

    def test_detail_news(self):
        # Create a news for test
        url = reverse('detail_news', kwargs={'pk': self.setUp().id})

        #user visit the page news/detail/id
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

        # user is redirected to the list of news
        resp = self.client.get('/v1/news')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'core/list_news.html')

    def test_create_news(self):
        before = New.objects.count()

        # user visit the page news/create
        
        url = reverse('create_news')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'core/create_news.html')
        self.assertContains(resp, 'Agrega una noticia')

        # user post data
        data = {'title': 'title', 'body': 'body'}
        resp = self.client.post(url, data, follow=True)
        self.assertEqual(resp.status_code, 200)

        # user is redirected to the list of news
        #resp = self.client.get('/v1/news')
        
        
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'core/list_news.html')
        self.assertEqual(New.objects.count(), before + 1)

    def test_delete_news(self):

        # Create a news for test
        url = reverse('delete_news', kwargs={'pk': self.setUp().id})
        before = New.objects.count()
        #user visit the page news/delete/id
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

        #user post data
        
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, 302)
    
        self.assertEqual(New.objects.count(), before - 1)

        # user is redirected to the list of news
        resp = self.client.get(reverse_lazy('list_news'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'core/list_news.html')

    def test_update_news(self):
        # Create a news for test
        url = reverse('update_news', kwargs={'pk': self.setUp().id})

        #user visit the page news/update/id
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

        # FIXME: No such file or directory
        #user post data
        data = {'title': 'title', 'body': 'new_body'}
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 302)

        # user is redirected to the list of news
        resp = self.client.get(url)
        self.assertContains(resp, 'new_body')
        self.assertEqual(resp.status_code, 200)

