from django import forms
from .models import Ouruser
from django.contrib.auth.hashers import check_password
class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages = {'required' : 'id를 입력해주세요'},
        max_length = 32, label='사용자 이름' )
    password = forms.CharField(
        error_messages = {'required' : 'pw를 입력해주세요'},
        widget = forms.PasswordInput, label='비밀번호' )

    def clean(self):
        cleaned_data = super().clean() #기존에 들어가있던 clean() 함수를 호출 -> 값이 들어있지 않다면 실패
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password: #빈값이 아니라면
            ouruser = Ouruser.objects.get(username = username)
            if not check_password(password, ouruser.password):
                self.add_error('password', '비밀번호가 틀렸습니다')
            else : 
                self.user_id = ouruser.id #user_id 를 form 에 넣어준다.
                