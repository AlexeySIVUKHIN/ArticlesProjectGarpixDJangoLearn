from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('articles/', ArticlesView.as_view()),
    path('comments/', CommentsView.as_view())
]

router = DefaultRouter()

router.register('articles2', ArticlesViewset)
router.register('comments2', CommentsViewset)

urlpatterns += router.urls