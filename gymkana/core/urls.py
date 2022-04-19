from django.contrib import admin
from django.urls import path
from .views import index, detail_news, list_news, create_news, delete_news

urlpatterns = [
    path('', index, name='index'),
    path('v1/news', list_news, name='list_news'),
    path('v1/news/<int:pk>/', detail_news, name='detail_news'),
    path('v1/news/create', create_news, name='create_news'),
    path('v1/news/<int:pk>/delete', delete_news, name='delete_news'),
]
