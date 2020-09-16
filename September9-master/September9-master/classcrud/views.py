from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import ClassBlog
from .forms import EditForm

def read(request):
    blogs = ClassBlog.objects.all()
    return render(request, 'classcrud/read.html', {'blogs':blogs})
    
def create(request):
    # 새로운 데이터 새로운 블로그 글 저장하는 역할 == POST
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')

    #입력된 블로그 글들을 저장해라         
    # 글쓰기 페이지를 띄워주는 역할 == GET
    else:
        #단순히 입력받을 수 있는 form을 띄어줘라
        form = EditForm()
        return render(request, 'classcrud/newblog.html', {'form':form} )


def update(request,pk):
    # 어떤 블로그를 수정할지 블로그 객체를 갖고오기
    blog = get_object_or_404(ClassBlog, pk = pk)
 
    # 해당하는 블로그 객체 pk에 맞는 입력공간 
    form = EditForm(request.POST, instance=blog)
    if form.is_valid():
            form.save()
            return redirect('home')
            
    return render(request, 'classcrud/newblog.html', {'form':form})

def delete(request,pk):
    blog = get_object_or_404(ClassBlog, pk = pk) # 어떤 블로그를 삭제할지 블로그 객체 갖고오기
    blog.delete() # 삭제
    return redirect('read')


