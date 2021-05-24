from django.test import TestCase
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.utils import timezone

from .models import New
from .forms import NewForm

# Create your tests here.
class NewsIndexTests(TestCase):

    def test_no_news(self):
        """
        If no news exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('news:index-1'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No news are available.")
        self.assertQuerysetEqual(response.context['latest_news_list'], [])

    def test_new_not_found(self):
        response = self.client.get(reverse('news:detail-1', args=[0]))
        self.assertEqual(response.status_code, 404)

class NewViewTests(TestCase):
    def setUp(self):
        New.objects.create(title="Primera noticia", subtitle="Empezamos a informar", body="Lorem ipsum", publish_date=timezone.now(), image=SimpleUploadedFile(name='erizo-hurra.jpg', content=open('/home/hmateo/Descargas/erizo-hurra.jpg', 'rb').read(), content_type='image/jpeg'))
        New.objects.create(title="Otra noticia", subtitle="Esto es periodismo", body="Lorem ipsum otra vez", publish_date=timezone.now())

        self.new_data = {
            'title': 'Testing new',
            'subtitle': 'Tests are to be done',
            'body': 'Lorem Ipsum',
            'publish_date': timezone.now(),
        }

        self.new_data_with_example_image = {
            'title': 'Testing new',
            'subtitle': 'Tests are to be done',
            'body': 'Lorem Ipsum',
            'publish_date': timezone.now(),
            'image': SimpleUploadedFile(
                name='default-news.jpeg',
                content=open('media/default/static/news/images/default-news.jpeg', 'rb').read(),
                content_type='image/jpeg'),
        }

    def test_first_news(self):
        """
        News are displayed on the index page.
        """

        response = self.client.get(reverse('news:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['latest_news_list'],
            ['<New: Otra noticia>', '<New: Primera noticia>']
        )

    def test_new_detail(self):

        first_new = New.objects.get(pk=1)
        response = self.client.get(reverse('news:detail', args=[first_new.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context['new'], first_new
        )

    def test_get_new_form(self):
        response = self.client.get(reverse('news:create-1'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div class="panel-heading">Create a New</div>', html=True)


    def test_post_new_form_success(self):
        response = self.client.post(reverse('news:create'), data=self.new_data)
        self.assertRedirects(response, "/news/v2/3/", status_code=302)

    def test_post_new_form_with_image_success(self):
        form = NewForm(data=self.new_data_with_example_image)
        response = self.client.post(reverse('news:create-1'), data=form.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['new'].image.name, 'default/static/news/images/default-news.jpeg')

    def test_get_update_new_form(self):
        first_new = New.objects.get(pk=1)
        response = self.client.get(reverse('news:update', args=[first_new.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div class="panel-heading">Editing ' + first_new.title + '</div>', html=True)

    def test_post_update_new_form(self):
        second_new = New.objects.get(pk=2)
        form = NewForm(
            data={
                'title': 'Una noticia editada',
                'subtitle': 'Se han cambiado los campos',
                'body': 'Nuevo texto',
            }
        )
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse('news:update-1', args=[second_new.id]), data=form.data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>' + form.data.get('title') + '</h1>', html=True)


    def test_update_new_form_fail(self):
        first_new = New.objects.get(pk=1)
        form = NewForm(
            data={
                'title' : None,
            }
        )
        self.assertFalse(form.is_valid())
        response = self.client.patch(reverse('news:update-1', args=[first_new.id]), data=form.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(form.errors["title"], ['This field is required.'])

    def test_get_delete_new(self):
        second_new = New.objects.get(pk=2)
        response = self.client.get(reverse('news:delete-1', args=[second_new.id]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Are you sure you want to delete this item?')

    def test_post_delete_new(self):
        second_new = New.objects.get(pk=2)
        response = self.client.delete(reverse('news:delete', args=[second_new.id]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['latest_news_list'],
            ['<New: Primera noticia>'])
        with self.assertRaises(New.DoesNotExist):
            New.objects.get(pk=2)

class NewFormValidationTests(TestCase):
    def setUp(self):
        self.data_with_invalid_image = {
            'title' : 'I wrote a new',
            'subtitle' : 'You will be interested',
            'body' : 'Lorem Ipsum',
            'publish_date' : timezone.now(),
            'image' : SimpleUploadedFile(
                name='requirements.txt',
                content=open('requirements.txt', 'rb').read(),
                content_type='text/plain'
            ),
        }

    def test_new_form_with_unsupported_image_type(self):
        form = NewForm(data=self.data_with_invalid_image)
        self.assertRaisesMessage(ValidationError, "Unsupported image type. Please upload jpeg or png.")
        self.assertFalse(form.is_valid())
        with self.assertRaisesMessage(ValidationError, "Unsupported image type. Please upload jpeg or png."):
            form.clean_image()