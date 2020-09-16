from django.urls import path
from . import views

urlpatterns = [
    path('read/', views.read, name="read"),
 # .as_view()는 우리가 상속받은 메소드들(ListView, CreateView 등등)에서 default로 저장되어있는 메소드
    path('newblog/', views.create, name='newblog'), # path 함수 안에 인자 -> url, 함수, urlpath 이름
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),

]