from django.shortcuts import render
from .forms import *
from django.contrib.auth import login, logout
# 이게 간지
from django.shortcuts import render, redirect
from users.models import User
# Create your views here.
def signup_view(request):
    if request.method == 'GET':

        # form = UserCreateForm #내가 만든 거 
        # form = UserCreationForm #장고가 만든 거
        form = SignUpForm #장고가만든걸 내가 커스터마이징
        context = {'form' : form}
        # Get으로 받아서 Post로 준다
        return render(request, 'accounts/signup.html', context)

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # form에 연결되어있는 model에 알아서 저장됨
            instance = form.save()
            return redirect('index')
            # #회원가입 처리 <- fields에 있는 것들
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password2']
        else :
            return redirect('accounts:signup')
        
def login_view(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html', { 'form' : AuthenticationForm()})
        #HTML 보여주기
    if request.method == 'POST':
        # form = SignUpForm(request.POST) #<- 얘는 유효성 검사 좀 빡심
        # #회원가입 처리 <- fields에 있는 것들
        # username = form.cleaned_data['username']
        # email = form.cleaned_data['email']
        # password = form.cleaned_data['password2']
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.user_cache)
            return redirect('index') 
        else :
            print("no")
            return render(request, 'accounts/login.html', {'form' : form})
        

def logout_view(request):
    #유효성 검사 -> 로그인일 때만
    #원래는 함수인데 property기능 때문에 () 안써도 되는거임
    if request.user.is_authenticated:
    #비즈니스 로직 처리 -> 로그아웃 진행
        logout(request)
    #응답
    return redirect('index')

