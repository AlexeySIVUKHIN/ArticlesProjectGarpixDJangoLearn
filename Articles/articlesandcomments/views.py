from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *
from django.contrib.auth.decorators import permission_required, login_required

def index(request):
    return HttpResponse('Текст')

def ArticlesList(request):
    a = Articles.objects.all()
    context = {
        'articles': a,
    }

    return render(request, 'articlesandcomments/articleslist.html', context)

def Article(request, art_slug):
    post = get_object_or_404(Articles, slug=art_slug)
    context = {
        'post': post,
    }
    return render(request, 'articlesandcomments/article.html', context = context)

def article_search(request):

    if request.method == 'GET':
        art_title = request.GET.get('art_title')
        f = None
        if art_title:
            f = Articles.objects.filter(title=art_title)
        context = {
            'articles': f,
            'title': art_title
        }
        return render(request, 'article_search.html', context = context)
@login_required()
def article_search_form(request):
    a = Articles.objects.all()
    context = {
        'articles': a,
    }

    return render(request, 'articlesandcomments/article_search_form.html', context)


