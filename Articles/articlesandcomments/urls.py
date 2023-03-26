from django.urls import path
from .views import *


urlpatterns = [
    path('index/', index),
    path('articleslist/', ArticlesList, name='articleslist'),
    path('article/<slug:art_slug>/', Article, name='article'),
    path('article_search/', article_search, name='article_search'),
    path('article_search_form/', article_search_form, name='article_search_form')

]