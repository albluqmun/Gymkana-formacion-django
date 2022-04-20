from django.contrib import admin
from django.urls import path
from .views import index, detail_news, list_news, create_news, delete_news, update_news
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('v1/news', list_news, name='list_news'),
    path('v1/news/<int:pk>/', detail_news, name='detail_news'),
    path('v1/news/create', create_news, name='create_news'),
    path('v1/news/<int:pk>/delete', delete_news, name='delete_news'),
    path('v1/news/<int:pk>/update', update_news, name='update_news'),
    path('v2/news', views.ListNews.as_view(), name='class_list_news'),
    path('v2/news/<int:pk>', views.DetailNews.as_view(), name='class_update_news'),
    path('v2/news/create', views.CreateNews.as_view(), name='class_create_news'),
    path('v2/news/<int:pk>/update', views.UpdateNews.as_view(), name='class_update_news'),
    path('v2/news/<int:pk>/delete', views.DeleteNews.as_view(), name='class_delete_news'),
]
