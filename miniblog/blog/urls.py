from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog'),
    path('post', views.index, name='blog_post'),
    path('post/new', views.update_post, name='update_post'),
    path('post/types', views.get_all_types, name='get_all_types'),
    path('post/tags', views.get_all_tags, name='get_all_tags'),
    path('post/<int:article_id>/', views.get_post_detail, name='get_post_detail'),
    path('post/delete/<int:article_id>/', views.delete_post, name='delete_post'),
    path('post/edit/<int:article_id>/', views.edit_post, name='edit_post'),
    path('post/author/<str:author_name>', views.find_by_author, name='find_by_author'),
    path('post/type/<str:type_name>', views.find_by_type, name='find_by_type'),
    path('post/tag/<str:tag_name>', views.find_by_tag, name='find_by_tag'),
]
