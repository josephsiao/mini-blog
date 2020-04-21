from datetime import datetime

from django.contrib.auth.models import User
# from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
# from django.views.generic.base import TemplateView
from django.template.response import TemplateResponse

from .models import Article, ArticleTag, ArticleType


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


def find_by_author(request, author_name):
    article_list = User.objects.filter(username=author_name).first().article_set.all()

    context = {
        'article_list': article_list
    }

    return render(request, 'index.html', context)


def find_by_type(request, type_name):
    article_list = ArticleType.objects.filter(type_name=type_name).first().articles.all()

    context = {
        'article_list': article_list
    }

    return render(request, 'index.html', context)


def find_by_tag(request, tag_name):
    article_list = ArticleTag.objects.filter(tag_name=tag_name).first().articles.all()

    context = {
        'article_list': article_list
    }

    return render(request, 'index.html', context)
