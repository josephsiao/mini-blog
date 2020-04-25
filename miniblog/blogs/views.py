from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .form import ArticlePostForm
from .models import Article, ArticleTag, ArticleType


def index(request):
    article_list = Article.objects.order_by('-published_time').all()

    context = {
        'article_list': article_list
    }

    return render(request, 'index.html', context)


def article_post(request, article_id):
    context = {
        'post': get_object_or_404(Article, pk=article_id),
        'post_tags': Article.objects.filter(id=article_id).values('article_tags__tag_name')
    }

    return render(request, 'blogs/article_post.html', context)


def find_by_author(request, author_name):
    article_list = User.objects.filter(username=author_name).first().article_set.all().order_by('-published_time')

    context = {
        'article_list': article_list
    }

    return render(request, 'index.html', context)


def find_by_type(request, type_name):
    article_list = ArticleType.objects.filter(type_name=type_name).first().articles.all().order_by('-published_time')

    context = {
        'article_list': article_list
    }

    return render(request, 'index.html', context)


def find_by_tag(request, tag_name):
    article_list = ArticleTag.objects.filter(tag_name=tag_name).first().articles.all().order_by('-published_time')

    context = {
        'article_list': article_list
    }

    return render(request, 'index.html', context)


@login_required
def add_new_post(request):
    if request.method == 'POST':
        data = dict(request.POST)

        article = Article()
        article.author = request.user
        article.title = data.get('title')[0]
        article.content = data.get('content')[0]
        article_type, _ = ArticleType.objects.get_or_create(type_name=data.get('article_type')[0])
        article.article_type = article_type
        article.save()

        for i in range(len(data.get('article_tags'))):
            article_tag, _ = ArticleTag.objects.get_or_create(tag_name=data.get('article_tags')[i])
            article.article_tags.add(article_tag)

        return redirect('/')
    else:
        form = ArticlePostForm()
        context = {
            'form': form
        }
        return render(request, 'blogs/edit_post.html', context)
