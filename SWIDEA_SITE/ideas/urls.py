from django.urls import path
from . import views

app_name = 'ideas'

urlpatterns = [
    path('', views.index, name='index'),  # 메인 페이지
    path('<int:idea_id>/', views.detail, name='detail'),  # 디테일 페이지
    path('create/', views.create, name='create'),  # 등록 페이지
    path('<int:idea_id>/edit/', views.edit, name='edit'),  # 수정 페이지
    path('<int:idea_id>/delete/', views.delete, name='delete'),  # 삭제 페이지
    path('<int:idea_id>/toggle-star/', views.toggle_star, name='toggle_star'),  # 찜하기 기능
    path('<int:idea_id>/adjust-interest-ajax/<str:adjustment>/', views.adjust_interest_ajax, name='adjust_interest_ajax'),  # 관심도 AJAX 조절
]