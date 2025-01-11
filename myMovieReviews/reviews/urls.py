from django.urls import path
from .views import *

app_name = 'reviews'

urlpatterns = [
    path('create/', review_create, name='review_create'),
    path('', review_list, name="review_list"),
    path("<int:pk>/", review_detail, name="review_detail"), 
    path("<int:pk>/update/", review_update, name='review_update'),
    path("<int:pk>/delete/", review_delete, name='review_delete'),
]

#<int:pk>
#특정 리뷰의 기본키를 URL로 전달받음
#정수 형태의 기본키 값을 URL에서 추출하여 -> View 함수에 전달 -> 해당 id의 디테일 페이지를 보여줌
#Django에서는 기본적으로 자동 증가하는 id필드을 기본키로 생성
#기본키 값은 폼을 제출하여 새 레코드를 생성할때마다 1부터 1씩 증가
#레코드를 삭제해도 id는 변하지 않음