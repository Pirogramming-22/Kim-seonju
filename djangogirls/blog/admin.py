from django.contrib import admin
from .models import Post

admin.site.register(Post) #관리자 페이지에서 Post모델을 보려면, 이 코드를 통해 모델을 등록