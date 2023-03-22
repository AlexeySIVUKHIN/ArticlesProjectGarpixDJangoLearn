from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('index/', index),
    path('articleslist/', ArticlesList),
    path('article/', Article),

]