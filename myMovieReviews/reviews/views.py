from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import MovieReviewForm

# Create your views here.

## 리뷰 작성
def review_create(request):
    if request.method=="POST":  # 폼 제출
        form = MovieReviewForm(request.POST) # POST 데이터를 기반으로 폼 생성
        if form.is_valid(): # 폼 데이터 유효성 검사
            form.save()     # 데베에 저장
            return redirect('reviews:review_list') # 저장 후 리스트 페이지로 리디렉션
    
    else:  # GET 요청 (폼을 작성할때) -> POST 
        form = MovieReviewForm() # 빈 폼을 생성하여 사용자에게 보여줌
    
    return render(request, 'review_form.html', {'form':form}) # {템플릿에서 사용할 이름: View 함수에서 생성한 객체} -> 템플릿 : {{form.as_p}}


##리뷰 리스트
def review_list(request):
    reviews = MovieReview.objects.all() #데베에 저장된 모든 리뷰를 가져옴(특정한 것만 가져올 때 : all -> filter(필드명=값)))
    return render(request, 'review_list.html', {'reviews':reviews})


##리뷰 디테일 페이지
#get_object_or_404() : 특정 조건에 맞는 객체를 조회하는 기능 / 만약, 조건에 맞는 객체가 있다면 해당 객체를 반환하고, 조건에 맞는 객체가 없으면 404 오류 페이지
def review_detail(request, pk): #기본키 값!!
    review = get_object_or_404(MovieReview, id=pk)
    return render(request, 'review_detail.html', {'review':review})
    
    
##리뷰 수정
#instance=review : 폼이 수정할 기본 객체를 지정, 기존 객체의 데이터를 새로운 데이터로 업데이트
def review_update(request, pk):
    review = get_object_or_404(MovieReview, id=pk) # 기존 리뷰
    
    if request.method == "POST": # 수정 제출
        form = MovieReviewForm(request.POST, instance=review) # 새로운 데이터(request.POST)를 기존 객체(review)에 덮어쓰도록 하는 역할
        if form.is_valid():
            form.save()
            return redirect('reviews:review_detail', pk=review.id) #수정된 리뷰의 디테일 페이지로 이동, 기본키 전달
        
    else : # 리뷰 수정 페이지에 처음 접속, Get 요청
        form = MovieReviewForm(instance=review) # 기존 데이터로 채워진 폼 생성
    
    return render(request, 'review_form.html', {'form':form})


## 리뷰삭제
def review_delete(request, pk):
    review = get_object_or_404(MovieReview, id=pk)
    
    if request.method == "POST": # 삭체 요청
        review.delete()
        return redirect("reviews:review_list")
    
    return render(request, 'review_confirm_delete.html', {'review':review}) # 사용자가 삭제 확인 페이지에 처음 접속할 때 발생, 식제 여부를 묻는 페이지가 렌더링 -> 사용자가 여기서 '삭제'버튼을 누르면 -> POST 요청이 발생