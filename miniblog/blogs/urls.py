from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs', views.index, name='index'),
    path('blogs/post', views.index, name='index'),
    path('blogs/post/add_new_post', views.add_new_post, name='add_new_post'),
    path('blogs/post/<int:article_id>/', views.article_post, name='article_post'),
    path('blogs/author/<str:author_name>', views.find_by_author, name='find_by_author'),
    path('blogs/type/<str:type_name>', views.find_by_type, name='find_by_type'),
    path('blogs/tag/<str:tag_name>', views.find_by_tag, name='find_by_tag'),
]
