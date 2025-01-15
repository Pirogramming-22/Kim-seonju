from django.shortcuts import render, redirect, get_object_or_404
from .forms import IdeaForm
from .models import *

# Create your views here.
# 메인페이지
from django.core.paginator import Paginator
def index(request):
    sort = request.GET.get('sort', 'latest')  # URL에서 'sort' 매개변수 가져오기 (기본값: 'latest')
    
    # 정렬 기준에 따라 아이디어 정렬
    if sort == 'name':
        idea_list = Idea.objects.all().order_by('title')  # 이름순 정렬
    elif sort == 'interest':
        idea_list = Idea.objects.all().order_by('-interest')  # 관심도(찜하기)순 정렬
    elif sort == 'oldest':
        idea_list = Idea.objects.all().order_by('id')  # 등록순(오래된 순) 정렬
    else:  # 기본값: 최신순 정렬
        idea_list = Idea.objects.all().order_by('-id')

    paginator = Paginator(idea_list, 4)  # 한 페이지에 4개의 아이디어 표시
    page_number = request.GET.get('page')  # 현재 페이지 번호 가져오기
    page_obj = paginator.get_page(page_number)  # 해당 페이지의 데이터 가져오기

    return render(request, 'ideas/index.html', {'page_obj': page_obj, 'sort': sort})


# 디테일 페이지
def detail(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)  # 단일 객체를 가져옴
    return render(request, 'ideas/detail.html', {'idea': idea})

# 등록 페이지
def create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES) #폼 데이터를 POST로부터 받고, 업로드된 파일(FILES)을 처리
        if form.is_valid():
            idea = form.save()
            return redirect('ideas:detail', idea_id=idea.id)
        
    else:
        form = IdeaForm()
        
    return render(request, 'ideas/create.html', {'form':form})


# 수정 페이지
def edit(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea) #기존 객체 수정
        if form.is_valid():
            form.save()
            return redirect('ideas:detail', idea_id=idea.id)
    else:
        form = IdeaForm(instance=idea)
    return render(request, 'ideas/edit.html', {'form': form, 'idea': idea})

#삭제 페이지
def delete(request, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    if request.method == 'POST':
        idea.delete()
        return redirect('ideas:index')
    return redirect('ideas:detail', idea_id=idea_id)

#찜하기
def toggle_star(request, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    idea.is_starred = not idea.is_starred  # 찜 상태를 반대로 변경
    idea.save()
    # next 파라미터 확인 후 리다이렉트
    next_url = request.GET.get('next', 'ideas:index')  # next가 없으면 메인 페이지로 리디렉션
    return redirect(next_url)

#관심도
from django.http import JsonResponse
def adjust_interest_ajax(request, idea_id, adjustment): # adjustment 인자:URL에서 increase 또는 decrease 값을 받아옴
    idea = get_object_or_404(Idea, pk=idea_id)
    
    if adjustment == 'increase':
        idea.interest += 1
    elif adjustment == 'decrease' and idea.interest > 0:
        idea.interest -= 1
    
    idea.save()
    
    # JSON 응답으로 현재 관심도 반환
    return JsonResponse({'interest': idea.interest})
