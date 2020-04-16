from django.contrib.auth.models import User
from django.db import models


class ArticleType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name


class ArticleTag(models.Model):
    tag_name = models.CharField(max_length=30)

    def __str__(self):
        return self.tag_name


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    published_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    article_type = models.ForeignKey(
        ArticleType,
        related_name='articles',
        on_delete=models.CASCADE
    )
    article_tags = models.ManyToManyField(
        ArticleTag,
        related_name='articles'
    )

    def __str__(self):
        return self.title
