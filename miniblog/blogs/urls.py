from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs', views.index, name='index'),
    path('blogs/post', views.index, name='index'),
    path('blogs/post/<int:article_id>/', views.article_post, name='article_post')
]
