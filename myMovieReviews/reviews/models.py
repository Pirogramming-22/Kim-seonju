from django.db import models

# Create your models here.
class MovieReview(models.Model):
    title = models.CharField(max_length=100) #CharField(max_length="") : 문자열 길이 제한
    year = models.IntegerField() #InterField: 정수 저장
    genre = models.CharField(max_length=100)
    rating = models.FloatField() #별점 (0.0 ~ 5.0)
    director = models.CharField(max_length=100)
    cast = models.TextField() 
    runtime = models.IntegerField()
    review_text = models.TextField()
    
    def __str__(self):     # __str__ 객체를 문자열로 표현할 떄
        return self.title  # title 를 반환
    
    
    
    