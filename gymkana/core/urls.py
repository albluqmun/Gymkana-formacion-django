from django.contrib import admin
from django.urls import path, re_path
from .views import index, detail_news, list_news, create_news, delete_news, update_news
from . import views

urlpatterns = [
    path('', index, name='index'),
    re_path(r'v1/news/?$', list_news, name='list_news'),
    path('v1/news/<int:pk>/', detail_news, name='detail_news'),
    path('v1/news/create', create_news, name='create_news'),
    path('v1/news/<int:pk>/delete', delete_news, name='delete_news'),
    path('v1/news/<int:pk>/update', update_news, name='update_news'),
    re_path(r'v2/news/?$', views.ListNews.as_view(), name='class_list_news'),
    path('v2/news/<int:pk>', views.DetailNews.as_view(), name='class_update_news'),
    path('v2/news/create', views.CreateNews.as_view(), name='class_create_news'),
    path('v2/news/<int:pk>/update', views.UpdateNews.as_view(), name='class_update_news'),
    path('v2/news/<int:pk>/delete', views.DeleteNews.as_view(), name='class_delete_news'),
    # Eventos
    re_path(r'v2/events/?$', views.ListEvent.as_view(), name='list_events'),
    path('v2/events/<int:pk>', views.DetailEvent.as_view(), name='detail_event'),
    path('v2/events/create', views.CreateEvent.as_view(), name='create_event'),
    path('v2/events/<int:pk>/update', views.UpdateEvent.as_view(), name='update_event'),
    path('v2/events/<int:pk>/delete', views.DeleteEvent.as_view(), name='delete_event'),

]
