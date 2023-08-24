from django.contrib import admin

# Register your models here.
from .models import Post, Comment

#테이블에 한 줄로 추가되는
class CommentInline(admin.TabularInline):
#comment가 model인
    model = Comment

# 보기 좋게 만들기 -> Post를 가져와서 추가하는데 내가 보여주고 싶은 양식으로
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin) :
    #()는 튜플 -> 불변성으로 인해 메모리 관리와 속도가 더 빠르다
    list_display = ('id', 'image', 'content', 'created_at', 'view_count', 'writer')
    list_editable = ('content', )
    list_filter = ('created_at', )
    search_fields = ('id', 'writer__username')
    search_help_text = "id랑 writer이름으로 검색하는 창"
    #[]는 리스트 -> 유동성
    #[] 리스트 안에는 클래스가 들어가야 한다.
    inlines = []

    actions = ['make_published']
    #3개를 고르면 queryset에 3개가 들어오고
    #현재ModelAdmin
    #HttpRequest현재 요청을 나타내는
    #QuerySet사용자가 선택한 개체 집합을 포함하는 입니다 .
    def make_published(modeladmin, request, queryset) :
        for item in queryset :
            item.content = '내 맘대로 수정'
            item.save()
    
