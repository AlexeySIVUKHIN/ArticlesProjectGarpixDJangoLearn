from rest_framework import serializers
from articlesandcomments.models import *

class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    art = ArticlesSerializer()
    class Meta:
        model = Comment
        fields = '__all__'