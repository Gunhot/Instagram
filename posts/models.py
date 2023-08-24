from django.db import models
#ORM -> model + querySet API
#model이 database를 만들어주고
#querySet API가 query 보내준다.
#filter, exclude, order_by() <= Set Return 
#get_or_create() <= 만들기
#update_or_create() <= 만들기
#count() <= int(return)
#get() <= 무조건 하나만 return!
#Query : 요청 // QuerySet : 응답(객체 여러개) // QuerySet API : 인터페이스
#함수를 call하면 Database로 알아서 query 보내준다.
#장고에서 만든 writer를 사용하자!

from django.contrib.auth import get_user_model
#가져와!!
User = get_user_model()

# Create your models here.
# Post는 model의 Model을 상속해서 만든다.
class Post(models.Model) :
    # image라는 이름의 속성 -> image field
    #verbose_name : aka
    #이미지 바로 처리하기 힘들어서 일단 비워둬
    image = models.ImageField(verbose_name="이미지", null =True, blank=True )
    content = models.TextField(verbose_name="내용")
    #자동으로 현재시간 입력되렴
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    view_count = models.IntegerField(verbose_name="조회수", default = 0)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null = True, blank = True)

class Comment(models.Model):
    content = models.TextField(verbose_name = "내용")
    created_at = models.DateTimeField(verbose_name="작성일")
    #얘는 Post의 PK를 foreign key로!
    #Post가 삭제되면 나도 삭제돼!
    post = models.ForeignKey(to='Post', on_delete=models.CASCADE)
    #writer는 장고가 만들어준다!
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE)