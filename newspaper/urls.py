from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('v1/news/create', views.create_news, name='create_news'),
    path('v1/news/view', views.news_view, name='news_view'),
    path('v1/news/view/<int:news_id>', views.news_view_detail, name='news_view_detail'),
    path('v1/news/view/update/<int:news_id>', views.news_update, name='news_update'),
    path('v1/news/view/delete/<int:news_id>', views.news_delete, name='news_delete'),
    path('v2/news/create', views.NewsCreate.as_view(), name='news_views_create_class'),
]
