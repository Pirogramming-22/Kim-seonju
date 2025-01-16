from django.db import models

# Create your models here.
class DevTool(models.Model):
    name = models.CharField(max_length=50)  # 개발 툴 이름
    kind = models.CharField(max_length=50)  # 개발 툴 종류 (예: 프레임워크, 라이브러리 등)
    content = models.TextField()  # 개발 툴 설명

    def __str__(self):
        return self.name