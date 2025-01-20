from django.urls import path
from . import views

apps_name = 'insta'
urlpatterns = [
    path('like_ajax/', views.like_ajax, name='like_ajax'),  # 좋아요 요청 처리
    path('', views.index, name='index'),     # 루트 URL 처리
    path('get_posts/', views.get_posts, name='get_posts'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('delete_comment/', views.delete_comment, name='delete_comment'),
]
