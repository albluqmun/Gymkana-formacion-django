from django.urls import path

from . import views

app_name = 'newspaper'

urlpatterns = [
    path('', views.IndexView.as_view(), name='newspaper'),
    path('<int:pk>/', views.NewView.as_view(), name='new'),
    path('<int:pk>/event/', views.EventView.as_view(), name='event'),
]
