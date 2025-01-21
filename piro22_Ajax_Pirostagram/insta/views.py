from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')  # index.html 템플릿 렌더링

def get_posts(request):
    if request.method == "GET":
        # 모든 게시물 조회
        posts = Post.objects.all()

        # 게시물과 댓글 데이터를 구성
        posts_data = []
        for post in posts:
            # 게시물에 연결된 댓글 가져오기
            comments = post.comments.all()  # related_name='comments'에 따라 연결된 댓글 가져오기
            comments_data = [{'id': comment.id, 'content': comment.content, 'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S')} for comment in comments]

            # 게시물 데이터와 댓글 데이터 포함
            posts_data.append({
                'id': post.id,
                'title': post.title,
                'likes': post.likes,
                'comments': comments_data  # 댓글 데이터 포함
            })

        return JsonResponse({'posts': posts_data})


#좋아요
def like_ajax(request):
    if request.method == "POST":
        data = json.loads(request.body) # 요청 본문에서 JSON 데이터 읽기 {id:1}
        post_id = data.get('id')
        post = Post.objects.get(id=post_id)
        post.likes += 1
        post.save()
        
        return JsonResponse({'id':post_id, 'likes':post.likes}) # 업데이트된 좋아요 수 반환

#댓글
@csrf_exempt  # CSRF 토큰을 처리하지 않도록 설정
def add_comment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post_id = data.get('post_id')
        content = data.get('content')
        
        post = Post.objects.get(id=post_id)
        comment = Comment.objects.create(post=post, content=content)
        
        return JsonResponse({
            'id': comment.id,
            'post_id': post.id,
            'content': comment.content,
            'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S')  # 문자열로 변환
        })  # JSON 응답 반환
        
#댓글 삭제
def delete_comment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        comment_id = data.get('comment_id')
        
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        
        return JsonResponse({'success': True})