import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Event

# Create your tests here.

class eventMethodTest(TestCase):


    def test_001_list_no_events(self):
        response = self.client.get(reverse('events:index_view'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['events'],[])


    def test_002_create_one_event(self):
        # import ipdb; ipdb.set_trace()
        response = self.client.post(reverse('events:create_view'), data={'title':'Good event', 'subtitle':'Subtitle', 'body':'Body', 
        'start_date':'2021-10-10 15:12', 'end_date':'2021-10-10 17:12'})
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('events:index_view'))
        self.assertQuerysetEqual(response.context['events'],['<event: Good event>'])


    def test_003_create_one_bad_event(self):
        response = self.client.post(reverse('events:create_view'), data={'title':'Bad event', 'subtitle':'Subtitle', 'body':'Body', 
        'start_date':'2021-10-10 15:12', 'end_date':'2021-09-10 15:12'})
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('events:index_view'))
        self.assertQuerysetEqual(response.context['events'],[])


    def test_004_create_one_good_and_one_bad_event(self):
        response = self.client.post(reverse('events:create_view'), data={'title':'Good event', 'subtitle':'Subtitle', 'body':'Body', 
        'start_date':'2021-10-10 15:12', 'end_date':'2021-10-10 17:12'})
        response = self.client.post(reverse('events:create_view'), data={'title':'Bad event', 'subtitle':'Subtitle', 'body':'Body', 
        'start_date':'2021-10-10 15:12', 'end_date':'2021-09-10 13:12'})
        response = self.client.get(reverse('events:index_view'))
        self.assertQuerysetEqual(response.context['events'],['<event: Good event>'])


    def test_005_create_two_events(self):
        response = self.client.post(reverse('events:create_view'), data={'title':'Good event 1', 'subtitle':'Subtitle', 'body':'Body', 
        'start_date':'2021-10-10 15:12', 'end_date':'2021-10-10 17:12'})
        response = self.client.post(reverse('events:create_view'), data={'title':'Good event 2', 'subtitle':'Subtitle', 'body':'Body', 
        'start_date':'2021-10-10 15:12', 'end_date':'2021-10-10 13:12'})
        response = self.client.get(reverse('events:index_view'))
        self.assertQuerysetEqual(response.context['events'],['<event: Good event 1>', '<event: Good event 2>'], ordered=False)

    
    def test_006_detail_event(self):
        response = self.client.post(reverse('events:create_view'), data={'title':'Good event', 'subtitle':'Subtitle', 'body':'Body', 
        'start_date':'2021-10-10 15:12', 'end_date':'2021-10-10 17:12'})
        response = self.client.get(reverse('events:detail_view', kwargs={'pk': Event.objects.get(title = 'Good event').id}))
        self.assertEqual(response.status_code, 200)
     

    def test_007_detail_event_not_valid(self):
        response = self.client.post(reverse('events:create_view'), data={'title':'Bad event - not valid', 'subtitle':'Subtitle', 'body':'Body', 
        'start_date':'2021-10-10 15:12', 'end_date':'2021-09-10 13:12'})      
        response = self.client.get(reverse('events:detail_view', kwargs={'pk': Event.objects.get(title = 'Bad event - not valid').id}))
        self.assertEqual(response.status_code, 404)


    def test_008_update_event_valid(self):
        response = self.client.post(reverse('events:create_view'), data={'title':'Good event - preview', 'subtitle':'Subtitle', 'body':'Body', 
        'start_date':'2021-10-10 15:12', 'end_date':'2021-10-10 17:12'})
        response = self.client.post(reverse('events:update_view', kwargs={'pk': Event.objects.get(title = 'Good event - preview').id}), 
        {'title':'Good event - updated', 'subtitle':'Subtitle', 'body':'Body', 'start_date':'2021-10-10 15:12', 'end_date':'2021-10-10 19:12'})
        self.assertRedirects(response, reverse('events:detail_view', kwargs={'pk': Event.objects.get(title = 'Good event - updated').id}))


    def test_009_update_event_not_valid(self):
        response = self.client.post(reverse('events:create_view'), data={'title':'Good event - preview', 'subtitle':'Subtitle', 'body':'Body', 
        'start_date':'2021-10-10 15:12', 'end_date':'2021-10-10 17:12'})
        response = self.client.post(reverse('events:update_view', kwargs={'pk': Event.objects.get(title = 'Good event - preview').id}), 
        {'title':'Bad event - updated', 'subtitle':'Subtitle', 'body':'Body', 'start_date':'2021-10-10 15:12', 'end_date':'2021-10-10 13:12'})
        self.assertEqual(response.status_code, 404)


    def test_010_delete_event(self):
        response = self.client.post(reverse('events:create_view'), data={'title':'Good event - preview', 'subtitle':'Subtitle', 'body':'Body', 
        'start_date':'2021-10-10 15:12', 'end_date':'2021-10-10 17:12'})
        response = self.client.delete(reverse('events:delete_view', kwargs={'pk': Event.objects.get(title = 'Good event - preview').id}))
        self.assertEqual(response.status_code, 302)
    

    def test_011_delete_event_not_exist(self):
        response = self.client.delete(reverse('events:delete_view', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, 404)


    def test_012_delete_and_get_event(self):
        response = self.client.post(reverse('events:create_view'), data={'title':'Good event - preview', 'subtitle':'Subtitle', 'body':'Body', 
        'start_date':'2021-10-10 15:12', 'end_date':'2021-10-10 17:12'})
        id = Event.objects.get(title = 'Good event - preview').id
        response = self.client.delete(reverse('events:delete_view', kwargs={'pk': id}))
        response = self.client.get(reverse('events:detail_view', kwargs={'pk': id}))
        self.assertEqual(response.status_code, 404)