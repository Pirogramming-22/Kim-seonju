from django.db import models

# Create your models here.
# upload_to : 저장경로, 
class Idea(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='idea_images/%Y/%m/%d/', blank=True, null=True)
    content = models.TextField()
    interest = models.PositiveBigIntegerField(default=0) #PositiveBigIntegerField : 0이상의 정수를 저장할 때 사용하는 필드 / default=0 : 기본값을 0으로 설정
    devtool = models.ForeignKey('tools.DevTool', on_delete=models.CASCADE, blank=False, null=False) # 개발 툴 (ForeignKey= 1대 다 관계 (1=tools.DevTool, 아이디어에 해당하는 개발툴은 하나))
    is_starred = models.BooleanField(default=False) # 찜 여부 필드 추가
    
    
    def __str__(self):
        return self.title