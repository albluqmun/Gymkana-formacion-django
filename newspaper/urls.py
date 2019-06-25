from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('v1/news/create', views.create_news, name='create_news'),
]
