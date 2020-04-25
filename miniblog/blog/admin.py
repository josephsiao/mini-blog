from django.contrib import admin

from .models import Article, ArticleTag, ArticleType


class AdminArticle(admin.ModelAdmin):
    autocomplete_fields = ['article_tags', 'article_type']


class AdminArticleTag(admin.ModelAdmin):
    search_fields = ['tag_name']


class AdminArticleType(admin.ModelAdmin):
    search_fields = ['type_name']


admin.site.register(Article, AdminArticle)
admin.site.register(ArticleType, AdminArticleType)
admin.site.register(ArticleTag, AdminArticleTag)
