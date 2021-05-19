from django.urls import path

from . import views

app_name = 'combi'
urlpatterns = [
    path('', views.index, name='index'),
]