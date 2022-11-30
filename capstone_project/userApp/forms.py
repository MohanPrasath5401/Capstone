from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile1,Profile3,Post,UpdatePost,comment

class SignUP(UserCreationForm):
    email = forms.EmailField(label='Email')
    class Meta:
        model = User
        fields =['username','email','password1','password2'] 


class Profile(forms.ModelForm):
    class Meta:
        model = Profile1
        fields = ['mobile','company_name','company_information']

class SignUP2(UserCreationForm):
    class Meta:
        model = User
        fields =['password1','password2'] 

class Profile2(forms.ModelForm):
    class Meta:
        model = Profile3
        fields = ['name','email','qualification','skills','experience']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content']

class UpdatePost(forms.ModelForm):
    class Meta:
        model = UpdatePost
        fields = ['no_of_opening','skills','experience']

class Comment(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['email','qualification','skills','experience']








