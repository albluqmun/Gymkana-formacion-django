from django.contrib import admin
from django.urls import path
from .views import index, detail_news, list_news

urlpatterns = [
    path('', index, name='index'),
    path('news/', list_news, name='list_news'),
    path('news/<int:pk>/', detail_news, name='detail_news'),
    
]
