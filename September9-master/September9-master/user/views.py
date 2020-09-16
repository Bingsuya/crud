from django.shortcuts import render, redirect
from .models import Ouruser
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password # 자동 암호화, 비밀번호 체크 기능
from .forms import LoginForm

def home(request):
    return render(request, 'home.html')
    
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username', None) # 앞에서 입력한 name필드에 있는 값을 key로 해서 전달
        useremail = request.POST.get('useremail', None) # 딕셔너리 형태이기 때문에 key가 없으면 에러가 남 -> get()함수로 기본값을 None으로 지정
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None) # 만약 key값이 없으면 기본값으로 None을 지정

        res_data = {} # 에러 메시지를 담을 변수

        if not (username and password and re_password): # 빈 문자열이 있거나 모든 값들이 다 들어있지 않다면
            res_data['error'] = '모든 값을 입력해주세요' # 에러 메시지 출력('error'라는 키와 문자열을 res_data에 넣는다)
        elif password != re_password: # 비밀번호가 다르다면
            res_data['error'] = '비번이 다릅니다....'
        else:
            ouruser = Ouruser( # 모델에서 만든 Ouruser를 가져와 생성
                username= username,
                useremail = useremail,
                password= make_password(password)
            )
            ouruser.save() # 저장
        #return render(request, 'home.html', res_data)
        return render(request, 'register.html', res_data)

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid(): #form 안에 있는 데이터가 정상적인지 확인
            request.session['user']= form.user_id
            return redirect('/')

    else : 
        form = LoginForm()

    return render(request, 'login.html', {'form' : form })

def logout(request):
    if request.session.get('user'): 
        del(request.session['user']) 
    return redirect('/')
