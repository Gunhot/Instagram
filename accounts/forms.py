from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# 안씀
class UserBaseForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'

# 안씀
class UserCreateForm(UserBaseForm):
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta(UserBaseForm.Meta):
        fields = ['username','email', 'phone', 'password', 'password2']

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email']