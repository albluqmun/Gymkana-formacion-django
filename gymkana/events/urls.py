from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'events'
urlpatterns = [
    path('v2/events/', views.IndexView.as_view(), name='index_view'),
    path('v2/events/create', views.CreateView.as_view(), name='create_view'),
    path('v2/events/detail/<int:pk>', views.DetailView.as_view(), name='detail_view'),
    path('v2/events/update/<int:pk>', views.UpdateView.as_view(), name='update_view'),
    path('v2/events/delete/<int:pk>', views.DeleteView.as_view(), name='delete_view'),

    path('api/events/', views.EventList.as_view(), name='event-list'),
    path('api/events/create', views.EventCreate.as_view(), name='event-create'),
    path('api/events/detail/<int:pk>', views.EventDetail.as_view(), name='event-detail'),
    path('api/events/update/<int:pk>', views.EventUpdate.as_view(), name='event-update'),
    path('api/events/delete/<int:pk>', views.EventDestroy.as_view(), name='event-destroy'),
    path('api/', include('rest_framework.urls')),

]