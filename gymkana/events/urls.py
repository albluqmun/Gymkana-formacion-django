from django.urls import path
from rest_framework import routers

from . import views

app_name = 'events'
router = routers.DefaultRouter()
urlpatterns = router.urls

urlpatterns = [
    path('v2/events/', views.IndexView.as_view(), name='index_view'),
    path('v2/events/create', views.CreateView.as_view(), name='create_view'),
    path('v2/events/detail/<int:pk>', views.DetailView.as_view(), name='detail_view'),
    path('v2/events/update/<int:pk>', views.UpdateView.as_view(), name='update_view'),
    path('v2/events/delete/<int:pk>', views.DeleteView.as_view(), name="delete_view")
]