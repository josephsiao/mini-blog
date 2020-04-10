from django.contrib import admin
from .models import Article, ArticleType, ArticleTag

admin.site.register(Article)
admin.site.register(ArticleType)
admin.site.register(ArticleTag)
