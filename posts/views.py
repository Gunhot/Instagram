from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.http import JsonResponse
# 장고에 있는 view중에서 listview를 사용
from django.views.generic.list import ListView
from .models import *

from .forms import *
# 로그인이 필요한 함수들
from django.contrib.auth.decorators import login_required

def index(request) :
    post_list = Post.objects.all().order_by('-created_at') #// all은 부담스럽다
    # html에 인자로 넘겨줄 것들
    context = {
        'post_list' : post_list
    }
    return render(request, 'index.html', context)
# 현재 경로에서 templates를 post_list.html을 찾아서 실행
# 없다면 templates에서 찾는다.

# 로그인이 안되어있으면 accounts-login이라는 녀석이 나온다.
@login_required
def post_list_view(request):
    # post_list = Post.objects.all() // all은 부담스럽다
    post_list = Post.objects.filter(writer=request.user)
    # html에 인자로 넘겨줄 것들
    context = {
        'post_list' : post_list
    }
    return render(request, 'posts/post_list.html', context)


def post_create_form_view(request):
    # 작성할 수 있는 곳을 줘!!
    if request.method == 'GET' :
        # 폼을 만든다음에 폼자체를 던져준다.
        form = PostCreateForm()
        # form = PostBaseForm()
        context = {
            'form' : form
        }
        return render(request, 'posts/post_form2.html', context)
    # 작성다했엉!
    else :
        # POST해서 받아온다
        # 사진은 FILES에서 받아온다.
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Post.objects.create(
                image=form.cleaned_data['image'],
                content=form.cleaned_data['content'],
                writer=request.user
                # 로그인하지 않았기 때문에 오류
                # writer=request.user,
            )
        else :
            return redirect('posts:post-create')
        return redirect('index')




def post_detail_view(request, id):
    # 하나를 불러오기
    # 없을 수도 있는 에러처리
    try :
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return redirect('index')
    context = {
        'post' : post,
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_update_view(request, id): 
    # post = Post.objects.get(id = id)
    # 404일때는 별도의 페이지 제작 그래서 괜찮음
    post = get_object_or_404(Post, id=id, writer = request.user)
    if request.method == 'GET' :
        context = {'post': post}
        return render(request, 'posts/post_form.html', context)
    else:
        new_image = request.FILES.get('image')
        content = request.POST.get('content')
        # 이전 이미지가 삭제되어야함
        if new_image :
            # 기존 이미지 삭제 
            post.image.delete()
            post.image = new_image
        # create와 차이가 발생하는 부분
        post.image = new_image
        post.content = content
        post.save()
        return redirect('posts:post-detail', post.id)


@login_required
def post_delete_view(request, id):
    post = get_object_or_404(Post, id=id, writer = request.user)
    # if request.user != post.writer :
        # return Http404('잘못된 접근입니다.')
    if request.method == 'GET' :
        context = {'post' : post}
        return render(request, 'posts/post_confirm_delete.html', context)
    else :
        post.delete()
        return redirect('index')




# 학습용
# # 로그인이 안되어있으면 accounts-login이라는 녀석이 나온다.
# @login_required
# def post_create_view(request):
#     if request.method == 'GET' :
#         return render(request, 'posts/post_form.html')
#     else :
#         image = request.FILES.get('image')
#         content = request.POST.get('content')
#         Post.objects.create(
#             image=image,
#             content=content,
#             # 로그인하지 않았기 때문에 오류
#             # writer=request.user,
#         )
#         return redirect('index')


# # Create your views here.
# def url_view(request):
#     # 괄호 안의 텍스트들은 text.html로
#     return HttpResponse('<h1>url_view</h1>')
#     # key : '' -> value : ""
#     data = {'code' : "001", 'msg' : "ok"}
#     return JsonResponse(data)

# # Path Parameter 방식 : url에서 들어온 path parameter는 괄호안에서 받을 수 있다.
# # Query 방식 : request를 사용해서 받는다.
# def url_parameter_view(request, username, test):
#     print(f'username : {username}')
#     print(f'test : {test}')
#     return HttpResponse()


# ## 이게 존나 신기한게 view.html은 뒤에 있는데 어떻게 받아온거냐
# def function_view(request) :
#     # form에서 쏘는 방식
#     # view.html이란 곳에서 보낼수도 있는 거잖아
#     if request.method == 'GET' :
#         print(f'request.GET : {request.GET}')
#     else :
#         print(f'request.POST : {request.POST}')
#     return render(request, 'view.html')

# #query set이 없으면 기본적으로 all로 생성이된다
# # class view는 model 설정이 필요하다
# class class_view(ListView) :
#     model = Post
#     ordering = ['-id']
#     # 기본 template은 해당 모델_list.html로 설정까지 됨 
#     # template 이름 설정이 필요하다

#     #둘다 됨!
#     template_name = 'posts/cbv_view.html'
#     # template_name = 'cbv_view.html'

# def function_list_view(request) :
#     #object_list를 직접 만들어줘야 함
#     #Post에는 총 3개의 데이터가 있음을 알 수 있다
#     #3, 2, 1
#     list = Post.objects.all().order_by('-id')
#     #list를 object_list를 사용할 수 있게 해준 것

#     return render(request, 'cbv_view.html', {'object_list' : list} )
