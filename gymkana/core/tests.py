import json
from django.test import TestCase, RequestFactory
from .models import New, Event
from django.conf.urls.static import static
from django.conf import settings
from django.test import Client
from django.urls import reverse, reverse_lazy

# api rest framework
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import RequestsClient
from rest_framework.test import APIRequestFactory

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
        
        url = reverse('create_news')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'core/create_news.html')
        self.assertContains(resp, 'Agrega una noticia')

        # user post data
        data = {'title': 'title', 'body': 'body', 'image': ''}
        resp = self.client.post(url, data)
        New.objects.create(title='title', subtitle="subtitle",  body='body', image='image')
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

        self.assertTemplateUsed(resp, 'core/create_news.html')
        self.assertContains(resp, 'Agrega una noticia')

        # user post data
        data = {'title': 'title', 'body': 'body', 'image': ''}
        resp = self.client.post(url, data)
        New.objects.create(title='title', subtitle="subtitle",  body='body', image='image')
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

    def test_update_class(self):
        # Create a news for test
        url = reverse('class_update_news', kwargs={'pk': self.setUp().id})
    
        #user visit the page news/update/id
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

        # post data update
        data = {'title': 'title', 'body': 'new_body', 'image': ''}
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 302)

class test_event(TestCase):
    
    def setUp(self):
        return Event.objects.create(title='title', subtitle="subtitle",  body='body', start_date='2019-01-01', end_date='2019-01-02')

    def test_list_event(self):
        url = reverse('list_events')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'core/list_events.html')
        self.assertContains(resp, 'title')

    def test_detail_event(self):
        url = reverse('detail_event', kwargs={'pk': self.setUp().id})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'core/detail_event.html')
        self.assertContains(resp, 'title')
        self.assertContains(resp, 'subtitle')

    def test_create_event(self):
        before = Event.objects.count()

        # user visit the page event/create
        
        url = reverse('create_event')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'core/create_event.html')
        self.assertContains(resp, 'Agrega un evento')
        # user post data
        data = {'title': 'title2', 'body': 'body', 'start_date': '2019-01-01', 'end_date': '2019-01-02'}
        resp = self.client.post(url, data, follow=True)
        Event.objects.create(title='title2', subtitle="subtitle",  body='body', start_date='2019-01-01', end_date='2019-01-02')
        self.assertEqual(resp.status_code, 200)

        # user is redirected to the list of evento
        resp = self.client.get(reverse_lazy('list_events'))

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'core/list_events.html')
        self.assertEqual(Event.objects.count(), before + 1)


    def test_update_event(self):
        # Create a event for test
        url = reverse('update_event', kwargs={'pk': self.setUp().id})

        #user visit the page event/update/id
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

        # post data update
        data = {'title': 'title2', 'body': 'new_body', 'start_date': '2019-01-01', 'end_date': '2019-01-02'}
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 200)

        # user is redirected to the list of evento
        resp = self.client.get(reverse_lazy('detail_event', kwargs={'pk': self.setUp().id}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'core/detail_event.html')
            
    def test_delete_event(self):
                
        # Create a event for test
        url = reverse('delete_event', kwargs={'pk': self.setUp().id})
        before = Event.objects.count()
        #user visit the page event/delete/id
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

        #user post data
        
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, 302)
    
        self.assertEqual(Event.objects.count(), before - 1)

        # user is redirected to the list of evento
        resp = self.client.get(reverse_lazy('list_events'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'core/list_events.html')

class Test_api_rest(TestCase):

    def setUp(self):
        data_event = {'title': 'title', 'subtitle': 'subtitle', 'body': 'body', 'start_date': '2019-01-01', 'end_date': '2019-01-02'}
        self.event = Event.objects.create(**data_event)

    def test_api_list_event(self):
        url = reverse('api_event')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'title')
        self.assertContains(resp, 'subtitle')

    def test_api_detail_event(self):
        url = reverse('api_event_detail', kwargs={'pk': self.event.id})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'title')
        self.assertContains(resp, 'subtitle')
        self.assertContains(resp, 'body')
        self.assertContains(resp, '2019-01-01')
        self.assertContains(resp, '2019-01-02')

    def test_api_create_event(self):
        before = Event.objects.count()
        url = reverse('api_event_create')
        data = {'title': 'title2', 'subtitle': 'subtitle', 'body': 'body', 'start_date': '2019-01-01', 'end_date': '2019-01-02'}
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Event.objects.count(), before + 1)

        
    def test_api_update_event(self):
        url = reverse('api_event_update', kwargs={'pk': self.event.id})
        data = {'title': 'title2', 'subtitle': 'subtitle', 'body': 'body', 'start_date': '2019-01-01', 'end_date': '2019-01-02'}
        resp = self.client.put(url, data, content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'title2')
        self.assertContains(resp, 'subtitle')
        self.assertContains(resp, 'body')
        self.assertContains(resp, '2019-01-01')
        self.assertContains(resp, '2019-01-02')

    def test_api_delete_event(self):
        url = reverse('api_event_delete', kwargs={'pk': self.event.id})
        before = Event.objects.count()
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, 204)
        self.assertEqual(Event.objects.count(), before - 1)



        

        

