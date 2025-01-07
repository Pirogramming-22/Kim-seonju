from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {}) #render 메서드를 호출하여 blog/post_list.html템플릿을 보여줌
