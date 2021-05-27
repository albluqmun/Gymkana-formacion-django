from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('v1/news/', views.index, name='index'),
    path('v1/news/create', views.create, name='create'),
    path('v1/news/detail/<int:id>', views.detail, name='detail'),
    path('v1/news/update/<int:id>', views.update, name="update"),

]