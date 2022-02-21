from django import http
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect

# Create your views here.
def Index(request):
    return HttpResponseRedirect(reverse('blog_app:blog_list'))