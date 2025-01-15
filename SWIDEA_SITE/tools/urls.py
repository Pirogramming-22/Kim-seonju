from django.urls import path
from . import views

app_name = 'tools'

urlpatterns = [
    path('', views.index, name='index'),  # 개발툴 목록 페이지
    path('create/', views.create, name='create'),  # 개발툴 등록 페이지
    path('<int:tool_id>/', views.detail, name='detail'),  # 개발툴 디테일 페이지
    path('<int:tool_id>/edit/', views.edit, name='edit'),  # 개발툴 수정 페이지
    path('<int:tool_id>/delete/', views.delete, name='delete'),  # 개발툴 삭제 기능
]
