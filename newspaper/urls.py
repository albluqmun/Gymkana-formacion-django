from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('v1/news/create', views.create_news, name='create_news'),
    path('v1/news/view', views.news_view, name='news_view'),
    path('v1/news/view/<int:news_id>', views.news_view_detail, name='news_view_detail'),
    path('v1/news/view/update/<int:news_id>', views.news_update, name='news_update'),
]
