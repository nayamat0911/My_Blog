from atexit import register
from urllib import request
from django.urls import reverse
from cmath import log
from re import A
import urllib
from django import forms
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate, login,logout

from .forms import ProfilePic, SignUpForm

# Create your views here.

# Sign up/registation session========================
def SignUp(request):
    form=SignUpForm()
    registered =False
    if request.method=="POST":
        form=SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered=True

    sign_context={
        'title':'Sign Up',
        'registered':registered,
        'Sign_form':form

    }
    return render(request,'login_app/signup.html',context=sign_context)


# Login session============================ 
from django.contrib.auth.forms import AuthenticationForm
def User_login(request):
    form=AuthenticationForm()
    if request.method == "POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request ,user)
                return render(request, 'login_app/profile.html')
    else:
        form=AuthenticationForm()
             
    login_context={
        "title":"Login",
        "login_form":form,
    }
    return render(request, 'login_app/login.html',context=login_context)


# Logout session==========================
def User_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog_app:HomePage'))


def User_profile(request):
    
    return render(request, 'login_app/profile.html',context={})


# Profile change session========================
from .forms import User_profile_Change_form
def User_change(request):
    current_user=request.user
    form=User_profile_Change_form(instance=current_user)
    if request.method == "POST":
        form = User_profile_Change_form(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form=User_profile_Change_form(instance=current_user)
            return HttpResponseRedirect(reverse('login_app:User_profile'))
    change_context={
        'title':'Change Profile',
        "change_form":form
    }
    return render(request, 'login_app/change_profile.html',context=change_context)
    

# Pass change session========================
def pass_change(request):
    current_user=request.user
    change=False
    form=PasswordChangeForm(current_user)
    if request.method == "POST":
        form=PasswordChangeForm(current_user,data=request.POST)
        if form.is_valid():
            form.save()
            change=True
            # return HttpResponseRedirect(reverse('login_app:User_profile'))
    pass_change_context={
        'title':'Pass Change',
        'pass_form':form,
        'changed':change
    }
    return render(request, 'login_app/change_pass.html',context=pass_change_context)




# Profile pic session========================
def add_pro_pic(request):
    form_=ProfilePic()
    if request.method == "POST":
        form_=ProfilePic(request.POST, request.FILES)
        if form_.is_valid():
            user_obj = form_.save(commit=False)
            user_obj.user=request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('login_app:User_profile'))
    pro_form={
        "title":"Profile Pic",
        'Pro_pic_frm':form_
    }
    return render(request, 'login_app/pro_pic.html',context=pro_form)


# Change Profile pic session========================
def change_pic(request):
    form__=ProfilePic(instance=request.user.user_profile)
    if request.method == "POST":
        form__ = ProfilePic(request.POST, request.FILES, instance=request.user.user_profile)
        if form__.is_valid():
            form__.save()
            return HttpResponseRedirect(reverse('login_app:User_profile'))
    pro_pic_chage={
        "title":"Chagne Pic",
        "Chang_pic_":form__,
    }
    return render(request, 'login_app/Re_change_pic.html',context=pro_pic_chage)


