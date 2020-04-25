from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.index, name='blog'),
    path('blog/post', views.index, name='blog_post'),
    path('blog/post/new', views.update_post, name='update_post'),
    path('blog/post/<int:article_id>/', views.get_post_detail, name='get_post_detail'),
    path('blog/post/delete/<int:article_id>/', views.delete_post, name='delete_post'),
    path('blog/post/edit/<int:article_id>/', views.edit_post, name='edit_post'),
    path('blog/post/author/<str:author_name>', views.find_by_author, name='find_by_author'),
    path('blog/post/type/<str:type_name>', views.find_by_type, name='find_by_type'),
    path('blog/post/tag/<str:tag_name>', views.find_by_tag, name='find_by_tag'),
]
