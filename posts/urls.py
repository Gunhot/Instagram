from django.urls import path

from .views import *

app_name = 'posts'

urlpatterns = [
    #이 url은 다른 파일에서 post-list라고 치환이 가능하다.
    path('', post_list_view, name = 'post-list'),
    path('new/', post_create_form_view, name = 'post-create'),
    path('<int:id>/', post_detail_view, name='post-detail'),
    path('<int:id>/edit/',post_update_view, name='post-update'),
    path('<int:id>/delete/',post_delete_view, name='post-delete'),
]