from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager
# manager : posts.objects.~
# 이름 같으면 문제여서 그럼
# User는 좀 특별해서 Manager관리해줘야함 ㄹㅇ
# DjangoUserManger들어가서 가져오셈
class UserManager(DjangoUserManager):
    # 일종의 기본~
    def _create_user(self, username, email, password, **extra_fields):
        # email 유효성 검사 예시
        if not email:
            raise ValueError('이메일 어디갓노')
        user = self.model(username=username, email=email, **extra_fields)
        # 암호화해서 넣기
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        # 얘는 추가로 넣어준거임
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        # 얘는 superuser니깐 true로
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, **extra_fields)
    


# 무조건 쓰는 것
class User(AbstractUser) :
    objects = UserManager()
    # post.objects.할 때 얘를 쓸 수 있게 되는 것
    # 추가 되는 것
    phone = models.CharField(max_length=11)


# 가끔 쓰는 것 (확장)
class UserInfo(models.Model) :
    phone_sub = models.CharField(max_length=11)
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
