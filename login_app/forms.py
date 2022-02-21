from dataclasses import field
import email
from pyexpat import model
from re import T
from statistics import mode
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(UserCreationForm):
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=('username', 'first_name','last_name' ,'email','password1','password2')

class User_profile_Change_form(UserChangeForm):
    class Meta:
        model=User
        fields=('username','email','first_name','last_name','password')

class ProfilePic(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=('profile_pic',)

