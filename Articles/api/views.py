from django.shortcuts import render
from articlesandcomments.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import viewsets

class ArticlesView(APIView):
    def get(self, request):
        articles = Articles.objects.all()
        serializer = ArticlesSerializer(articles, many=True)
        return Response({'articles':serializer.data})

    def post(self, request):
        article = request.data.get('article')

        serializer = ArticlesSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            saved_data = serializer.save()
        return Response({"success": "Article '{}' created succesfully".format(saved_data.title)}, status=201)

class CommentsView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentsSerializer(comments, many=True)
        return Response({'comments':serializer.data})

    def post(self, request):
        comments = request.data.get('comments')

        serializer = CommentsSerializer(data=comments)
        if serializer.is_valid(raise_exception=True):
            saved_data = serializer.save()
        return Response({"success": "Comment '{}' created succesfully".format(saved_data.name)}, status=201)


class ArticlesViewset(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer

class CommentsViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer