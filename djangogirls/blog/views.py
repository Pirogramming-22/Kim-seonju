from django.shortcuts import render
from django.utils import timezone
from .models import Post #model.py 파일에 있는 Post 객체를 불러옴

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts}) #render 메서드를 호출하여 blog/post_list.html템플릿을 보여줌