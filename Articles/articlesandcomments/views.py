
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
def index(request):
    return HttpResponse('Текст')
def ArticlesList(request):
    a = Articles.objects.all()
    context = {
        'articles': a,
    }

    return render(request, 'articlesandcomments/articleslist.html', context)

def Article(request, art_id):
    post = get_object_or_404(Articles, id=art_id)
    context = {
        'post': post,

    }
    return render(request, 'articlesandcomments/article.html', context = context)



#
# def Article(request):
#     post = get_comments.all()
#     context = {'post': post,
#                'title': Articles.title
#     }
#
#     return render(request, 'articlesandcomments/article.html', context = context)
