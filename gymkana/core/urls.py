from django.contrib import admin
from django.urls import path
from .views import index, detail_news

urlpatterns = [
    path('', index, name='index'),
    path('news/<int:pk>/', detail_news, name='detail_news'),
]
