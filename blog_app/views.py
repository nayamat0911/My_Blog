from ast import Return
from dataclasses import field
from re import template
import re
from tkinter.messagebox import RETRY
from urllib import request
from django.shortcuts import render,HttpResponseRedirect, HttpResponse, redirect
from django.views.generic import CreateView, UpdateView, ListView,DetailView,View ,TemplateView,DeleteView
from django.urls import reverse , reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from django import forms
from blog_app.models import Blog,Likes,Comment
from .forms import CommentForm, UpdatePost
# Create your views here.
# def Blog_list(request):
#     return render(request, 'blog_app/blog_list.html')


class CreateBlog(LoginRequiredMixin ,CreateView):
    model = Blog
    template_name = 'blog_app/create_blog.html'
    fields = ('blog_title', 'blog_content', 'blog_image',)
    
    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('blog_app:HomePage'))


class BlogList(ListView):
    context_object_name="blogs"
    model = Blog
    template_name = 'blog_app/blog_list.html'
    # queryset = Blog.objects.order_by('-publish_date') #for  blog post time ordering 



@login_required
def blog_details(request,slug):
    blog = Blog.objects.get(slug=slug)
    comment_form=CommentForm()
    already_liked = Likes.objects.filter(blog=blog, user=request.user)
    if already_liked:
        liked =True
    else:
        liked= False

    if request.method == "POST":
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.user=request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('blog_app:blog_list'))

    details_context={
        'title':'Blog Details',
        'blog':blog,
        'comment_form':comment_form,
        'liked__':liked
    }
    return render(request, 'blog_app/blog_details.html',context=details_context)

@login_required
def liked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog, user=user)
    if not already_liked:
        liked_post= Likes(blog=blog, user=user)
        liked_post.save()
    return redirect('blog_app:blog_list')

@login_required
def unliked(request, pk):
    blog= Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog, user=user)
    already_liked.delete()
    
    return redirect('blog_app:blog_list')


class MyBlogs(LoginRequiredMixin, TemplateView):
    template_name='blog_app/my_blogs.html'

       
class UpdateBlog(LoginRequiredMixin,UpdateView):
    model = Blog
    template_name='blog_app/edit_blog.html'
    fields=['blog_title','blog_image','blog_content']

    def get_success_url(self):
        return reverse_lazy('blog_app:my_blog')
    
class RemovePost(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = "blog_app/delete_blog.html"
    success_url = reverse_lazy('blog_app:my_blog')
   
#for paginator
from django.core.paginator import Paginator
def HomePage(request):
    post_list=Blog.objects.all()
    blog_paginator=Paginator(post_list, 5)
    page_number = request.GET.get('page')
    pag_obj = blog_paginator.get_page(page_number)
    post_list_con={
        "title":"Blog_post",
        "blogs_title_obj":post_list,
        'post_object':pag_obj
    }
    return render(request,'blog_app/homepage.html', context=post_list_con)


def Read_page(request):
    read_context={
        "title":"Reader",
    }
    return render (request, 'blog_app/Read_more.html', context=read_context)