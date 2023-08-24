from django.contrib import admin
from django.urls import path, include

# 사용자들이 작성한 이미지를 사용하기 위함
from django.conf import settings
from django.conf.urls.static import static

from posts.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    # 이 url은 index라 불린다.
    
    path('accounts/', include('accounts.urls', namespace = 'accounts')),
    path('posts/', include('posts.urls', namespace = 'posts')),
    # 디버그 툴바 사용
    path("__debug__/", include("debug_toolbar.urls")),
]

# 사용자들이 작성한 이미지를 넣기 위함
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    # 변수를 넣어주는 법
    # path('url/<str:username>/<int:test>', url_parameter_view),
    # path('url/', url_view),
    # path('fbv/', function_view),
    # #class_view는 클래스이기 때문에 as_view로 바꿔준다
    # # path('cbv/', class_view.as_view()),
    # path('cbv/', function_list_view),