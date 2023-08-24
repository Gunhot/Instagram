from django import forms
from .models import *
# # 우선 폼 상속 받기
# class PostBaseForm(forms.Form) :
#     CATEGORY_CHOICES = [
#         ('1', '일반'),
#         ('2', '계정')
#     ]
#     image = forms.ImageField()
#     content = forms.CharField(widget=forms.Textarea)
#     category = forms.ChoiceField(choices=CATEGORY_CHOICES)

# 간지 Form
# 이것이 간지
class PostBaseForm(forms.ModelForm) :
    # 얘는 Post의 모든 것을 입력받아줍니다.
    class Meta:
        model = Post
        fields = '__all__'

from django.core.exceptions import ValidationError
class PostCreateForm(PostBaseForm) :
    class Meta(PostBaseForm.Meta) :
        # 안그럼 조회수랑 writer도 나옴
        fields = ['image', 'content']

# def clean쓰면 싹다 할 수도 있음 -> 공식문서 참고
    def clean_content(self) :
        data = self.cleaned_data['content']
        if "비속어" == data :
            raise ValidationError["비속어쓰지마셈"]
        return data


class PostUpdateForm(PostBaseForm) :
    class Meta(PostBaseForm.Meta) :
        # 안그럼 조회수랑 writer도 나옴
        fields = ['image', 'content']

class PostDetailForm(PostBaseForm) :
    class Meta(PostBaseForm.Meta) :
        # 안그럼 조회수랑 writer도 나옴
        fields = ['image', 'content']