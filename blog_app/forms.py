from dataclasses import field
from django import forms
from .models import Likes , Comment,Blog



class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('comment',)


class UpdatePost(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('blog_title','blog_content','blog_image')