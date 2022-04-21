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
        self.event = Event.objects.create(title='title', subtitle = "subtitle", body='body', start_date='2019-01-01', end_date='2019-01-02')
        return New.objects.create(title='title', subtitle="subtitle",  body='body', image='image')

    def test_index_get_list_news(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')
        self.assertContains(response, 'title')
    
    def test_list_news_get(self):
        
        url = reverse_lazy('list_news')
        resp = self.client.get(url, follow=True)

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'core/list_news.html')
        self.assertContains(resp, 'title')
        self.assertContains(resp, 'subtitle')

    def test_detail_news(self):
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
        data = {'title': 'title', 'body': 'body', 'image': ''}
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 200)

        # user is redirected to the list of news
        resp = self.client.get(reverse_lazy('list_news'))
        
        
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'core/list_news.html')
        # FIXME: Fail: AssertionError: 1 != 2
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

    #FIXME: ERROR: No such file or directory: image
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


class TestViewClassNews(TestCase):

    def setUp(self):
        return New.objects.create(title='title', subtitle="subtitle",  body='body', image='image')

    def test_list_class(self):
        url = reverse('class_list_news')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'core/class_list_news.html')
        self.assertContains(resp, 'title')
        self.assertContains(resp, 'subtitle')

    def test_detail_class(self):
        url = reverse('class_detail_news', kwargs={'pk': self.setUp().id})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'core/class_detail_news.html')
        self.assertContains(resp, 'title')
        self.assertContains(resp, 'subtitle')

    def test_create_class(self):
        before = New.objects.count()

        # user visit the page news/create
        
        url = reverse('class_create_news')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

        # FIXME: FAIL: No such file or directory
        self.assertTemplateUsed(resp, 'core/class_create_news.html')
        self.assertContains(resp, 'Agrega una noticia')

        # user post data
        data = {'title': 'title', 'body': 'body', 'image': ''}
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 200)

        # user is redirected to the list of news
        resp = self.client.get(reverse_lazy('class_list_news'))
        
        
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'core/class_list_news.html')
        self.assertEqual(New.objects.count(), before + 1)

    def test_delete_class(self):

            
        # Create a news for test
        url = reverse('class_delete_news', kwargs={'pk': self.setUp().id})
        before = New.objects.count()
        #user visit the page news/delete/id
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

        #user post data
        
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, 302)
    
        self.assertEqual(New.objects.count(), before - 1)

        # user is redirected to the list of news
        resp = self.client.get(reverse_lazy('class_list_news'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'core/class_list_news.html')
        
    #FIXME: ERROR: keyError:'start_date'
    def test_update_class(self):
        # Create a news for test
        url = reverse('class_update_news', kwargs={'pk': self.setUp().id})
    
        #user visit the page news/update/id
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

        # post data update
        data = {'title': 'title', 'body': 'new_body'}
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 302)
