from django.urls import path

from . import views

app_name = 'portal'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index.html'),
    path('v1/news/create', views.create_new, name = 'new_form'),
    path('v1/news/<int:new_id>', views.read_new, name = 'read_new'),
    ]