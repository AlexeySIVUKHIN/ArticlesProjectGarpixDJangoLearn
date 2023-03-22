from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('index/', index),
    path('articleslist/', ArticlesList, name='articleslist'),
    # path('article/', Article),
    path('article/<int:art_id>/', Article, name='article'),

]