from django.contrib import admin

from .models import Article, ArticleTag, ArticleType

admin.site.register(Article)
admin.site.register(ArticleType)
admin.site.register(ArticleTag)
