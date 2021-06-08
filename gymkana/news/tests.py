import datetime
from io import BytesIO
from django.core.files.uploadedfile import TemporaryUploadedFile
from django.urls import reverse
from django.utils import timezone
from django.test import TestCase
from .models import New
from gymkana.settings import BASE_DIR, MEDIA_URL

# Create your tests here.

def open_image(image):
    return TemporaryUploadedFile(BASE_DIR + MEDIA_URL + image)


class NewMethodTest(TestCase):


    def test_001_list_no_news(self):
        response = self.client.get(reverse('news:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['news'],[])

    
    def test_002_create_new(self):
        image = open_image('default.jpg')
        response = self.client.post(reverse('news:create'), data={'title':'Good new', 'subtitle':'Subtitle', 'body':'Body', 
        'days':2, 'image':image})
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('news:index'))
        self.assertQuerysetEqual(response.context['news'],['<New: Good new>'])

    
    def test_003_create_new_bad_mimetype(self):
        image = open(BASE_DIR + MEDIA_URL + 'yuhugasolina.gif', 'rb')
        response = self.client.post(reverse('news:create'), data={'title':'Bad new', 'subtitle':'Subtitle', 'body':'Body', 
        'days':2, 'image':image})
        response = self.client.get(reverse('news:index'))
        self.assertQuerysetEqual(response.context['news'],[])

    
    def test_004_create_new_image_bad_size(self):
        image = open(BASE_DIR + MEDIA_URL + 'Pano-bayer-leverkusen.jpg', 'rb')
        response = self.client.post(reverse('news:create'), data={'title':'Bad new - bad_size', 'subtitle':'Subtitle', 'body':'Body', 
        'days':2, 'image':image})
        response = self.client.get(reverse('news:index'))
        self.assertQuerysetEqual(response.context['news'],[])


    def test_005_create_one_good_and_one_bad_new(self):
        image1 = open(BASE_DIR + MEDIA_URL + 'default.jpg', 'rb')
        image2 = open(BASE_DIR + MEDIA_URL + 'yuhugasolina.gif', 'rb')
        response = self.client.post(reverse('news:create'), data={'title':'Good new', 'subtitle':'Subtitle', 'body':'Body', 
        'days':2, 'image':image1})
        response = self.client.post(reverse('news:create'), data={'title':'Bad new', 'subtitle':'Subtitle', 'body':'Body', 
        'days':2, 'image':image2})
        response = self.client.get(reverse('news:index'))
        self.assertQuerysetEqual(response.context['news'],['<New: Good new>'])


    def test_006_create_two_news(self):
        image1 = open(BASE_DIR + MEDIA_URL + 'default.jpg', 'rb')
        image2 = open(BASE_DIR + MEDIA_URL + 'default.jpg', 'rb')
        response = self.client.post(reverse('news:create'), data={'title':'Good new 1', 'subtitle':'Subtitle', 'body':'Body', 
        'days':2, 'image':image1})
        response = self.client.get(reverse('news:index'))
        response = self.client.post(reverse('news:create'), data={'title':'Good new 2', 'subtitle':'Subtitle', 'body':'Body', 
        'days':2, 'image':image2})
        response = self.client.get(reverse('news:index'))
        self.assertQuerysetEqual(response.context['news'],['<New: Good new 1>', '<New: Good new 2>'], ordered=False)

    
    def test_007_detail_new(self):
        image = open(BASE_DIR + MEDIA_URL + 'default.jpg', 'rb')
        response = self.client.post(reverse('news:create'), data={'title':'Good new', 'subtitle':'Subtitle', 'body':'Body', 
        'days':2, 'image':image})
        response = self.client.get(reverse('news:detail', kwargs={'id': New.objects.get(title = 'Good new').id}))
        self.assertEqual(response.status_code, 200)


    def test_008_update_new_valid(self):
        image = open(BASE_DIR + MEDIA_URL + 'default.jpg', 'rb')
        response = self.client.post(reverse('news:create'), data={'title':'Good new - preview', 'subtitle':'Subtitle', 'body':'Body', 
        'days':2, 'image':image})
        response = self.client.put(reverse('news:update', kwargs={'id': New.objects.get(title = 'Good new - preview').id}), 
        {'title':'Good new - updated', 'subtitle':'Subtitle', 'body':'Body', 'days':'2021-10-12 21:20', 'image':image})
        self.assertRedirects(response, reverse('news:detail', kwargs={'id': New.objects.get(title = 'Good new - updated').id}))


    
    def test_009_update_new_not_valid(self):
        image1 = open(BASE_DIR + MEDIA_URL + 'default.jpg', 'rb')
        image2 = open(BASE_DIR + MEDIA_URL + 'Pano-bayer-leverkusen.jpg', 'rb')
        response = self.client.post(reverse('news:create'), data={'title':'Good new - preview', 'subtitle':'Subtitle', 'body':'Body', 
        'days':2, 'image':image1})
        response = self.client.post(reverse('news:update', kwargs={'id': New.objects.get(title = 'Good new - preview').id}), 
        {'title':'Bad new - updated', 'subtitle':'Subtitle', 'body':'Body', 'days':'2021-10-12 21:20', 'image': image2})
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse('news:index'))
        self.assertQuerysetEqual(response.context['news'],['<New: Good new - preview>'])
    

    def test_010_delete_new(self):
        image = open(BASE_DIR + MEDIA_URL + 'default.jpg', 'rb')
        response = self.client.post(reverse('news:create'), data={'title':'Good new - preview', 'subtitle':'Subtitle', 'body':'Body', 
        'days':2, 'image':image})
        response = self.client.delete(reverse('news:delete', kwargs={'id': New.objects.get(title = 'Good new - preview').id}))
        self.assertEqual(response.status_code, 302)
    

    def test_011_delete_new_not_exist(self):
        response = self.client.delete(reverse('news:delete', kwargs={'id': 2}))
        self.assertEqual(response.status_code, 404)


    def test_012_delete_and_get_new(self):
        image = open(BASE_DIR + MEDIA_URL + 'default.jpg', 'rb')
        response = self.client.post(reverse('news:create'), data={'title':'Good new - preview', 'subtitle':'Subtitle', 'body':'Body', 
        'days':2, 'image':image})
        id = New.objects.get(title = 'Good new - preview').id
        response = self.client.delete(reverse('news:delete', kwargs={'id': id}))
        response = self.client.get(reverse('news:detail', kwargs={'id': id}))
        self.assertEqual(response.status_code, 404)

   


