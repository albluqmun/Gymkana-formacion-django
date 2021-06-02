from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('v1/news/', views.index, name='index'),
    path('v1/news/create', views.create, name='create'),
    path('v1/news/detail/<int:id>', views.detail, name='detail'),
    path('v1/news/update/<int:id>', views.update, name="update"),
    path('v1/news/delete/<int:id>', views.delete, name="delete"),
    path('v2/news/', views.IndexView.as_view(), name='index_view'),
    path('v2/news/create', views.CreateView.as_view(), name='create_view'),
    path('v2/news/detail/<int:pk>', views.DetailView.as_view(), name='detail_view'),
    path('v2/news/update/<int:pk>', views.UpdateView.as_view(), name='update_view'),
    path('v2/news/delete/<int:pk>', views.DeleteView.as_view(), name="delete_view"),

]