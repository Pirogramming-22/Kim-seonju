from django import forms
from .models import *

#forms.ModelForm : Django가 제공하는 폼 클래스, 모델과 연결된 폼을 자동으로 생성
class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview  # 폼이 참조할 모델 설정
        fields = ['title', 'year', 'genre', 'rating', 'runtime', 'director', 'cast', 'review_text']
