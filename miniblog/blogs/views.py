from datetime import datetime

# from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
# from django.views.generic.base import TemplateView
from django.template.response import TemplateResponse

from .models import Article, ArticleTag


def index(request):
    context = {
        'article_list': Article.objects.values()
    }

    return render(request, 'index.html', context)


def article_post(request, article_id):
    context = {
        'post': get_object_or_404(Article, pk=article_id),
        'post_tags': Article.objects.filter(id=article_id).values('article_tags__tag_name')
    }

    return render(request, 'blogs/article_post.html', context)
