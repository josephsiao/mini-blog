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


def get_post_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article_tags = [tag.tag_name for tag in article.article_tags.all()]

    context = {
        'article': article,
        'article_tags': article_tags
    }

    return render(request, 'blog/post_detail.html', context)


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
def update_post(request):
    if request.method == 'POST':
        data = dict(request.POST)

        if data.get('edit_id'):
            article = Article.objects.get(id=data.get('edit_id')[0])
        else:
            article = Article()

        article.author = request.user
        article.title = data.get('title')[0]
        article.content = data.get('content')[0]
        article.article_type, _ = ArticleType.objects.get_or_create(type_name=data.get('article_type')[0])
        article.save()

        article_tags = []
        for i in range(len(data.get('article_tags'))):
            article_tag, _ = ArticleTag.objects.get_or_create(tag_name=data.get('article_tags')[i])
            article_tags.append(article_tag)

        article.article_tags.set(article_tags)

        return redirect('/')
    else:
        form = ArticlePostForm()

        context = {
            'form': form
        }

        return render(request, 'blog/edit_post.html', context)


@login_required
def delete_post(request, article_id):
    if Article.objects.filter(id=article_id).exists():
        article = Article.objects.get(id=article_id)

        if article.author == request.user:
            article.delete()

    return redirect('/')


@login_required
def edit_post(request, article_id):
    if Article.objects.filter(id=article_id).exists():
        article = Article.objects.get(id=article_id)
        article_tags = [tag.tag_name for tag in article.article_tags.all()]

        if article.author == request.user:
            form = ArticlePostForm(initial={
                'title': article.title,
                'content': article.content
            })

            context = {
                'form': form,
                'article': article,
                'article_tags': article_tags
            }

            return render(request, 'blog/edit_post.html', context)

    return redirect('/')
