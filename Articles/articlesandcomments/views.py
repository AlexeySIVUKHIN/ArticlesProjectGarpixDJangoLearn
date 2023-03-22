
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def ArticlesList(request):
    articles_page = Articles.objects.all()
    context = {'articles_page': articles_page,
               'title': 'Список статей'
    }

    return render(request, 'articlesandcomments/articleslist.html', context = context)

def index(request):
    return HttpResponse('Текст')

def Article(request):
    post = Articles.objects.all()
    context = {'post': post,
               'title': Articles.title
    }

    return render(request, 'articlesandcomments/article.html', context = context)
