from django.shortcuts import render, get_object_or_404, redirect
from .models import DevTool
from .forms import DevToolForm

# Create your views here.
# 개발툴 목록 페이지
def index(request):
    tools = DevTool.objects.all()
    return render(request, 'tools/index.html', {'tools': tools})

# 등록 페이지
def create(request):
    if request.method == 'POST':
        form = DevToolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tools:index')
    else:
        form = DevToolForm()
    return render(request, 'tools/create.html', {'form': form})


# 디테일 페이지
def detail(request, tool_id):
    tool = get_object_or_404(DevTool, pk=tool_id)
    ideas = tool.idea_set.all()  # 해당 개발툴을 사용한 아이디어 목록
    return render(request, 'tools/detail.html', {'tool': tool, 'ideas': ideas})

# 수정 페이지
def edit(request, tool_id):
    tool = get_object_or_404(DevTool, pk=tool_id)
    if request.method == 'POST':
        form = DevToolForm(request.POST, instance=tool)
        if form.is_valid():
            form.save()
            return redirect('tools:detail', tool_id=tool.id)
    else:
        form = DevToolForm(instance=tool)
    return render(request, 'tools/edit.html', {'form': form, 'tool': tool})


# 삭제 페이지
def delete(request, tool_id):
    tool = get_object_or_404(DevTool, pk=tool_id)
    if request.method == 'POST':
        tool.delete()
        return redirect('tools:index')
    return redirect('tools:detail',tool_id=tool_id)

