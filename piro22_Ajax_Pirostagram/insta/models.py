from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    likes = models.IntegerField()
    
    def __str__(self):
        return self.title
    
#댓글
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField() # 댓글 내용
    created_at = models.DateTimeField(auto_now_add=True) # 댓글 작성 시간
    
    def __str__(self):
        return self.context[:20] # 댓글 내용의 일부만 반환