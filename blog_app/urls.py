from django.urls import path
from .import views
from .views import CreateBlog,BlogList, UpdateBlog

app_name='blog_app'

urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('all/', views.BlogList.as_view(), name='blog_list'),
    path('write/', views.CreateBlog.as_view(),name='create_blog' ),
    path('details/<slug>', views.blog_details, name='blog_details'),
    path('liked/<pk>/', views.liked, name='liked_post'),
    path('unliked/<pk>/', views.unliked, name='unliked_post'),
    path('my-blog/', views.MyBlogs.as_view(), name='my_blog'),
    path('edit-blog/<int:pk>/', views.UpdateBlog.as_view(), name='edit_blog'),
    path('delete-blog/<int:pk>/', views.RemovePost.as_view(), name='delete_blog'),
    path('reader/', views.Read_page, name='Read_page'),
    
]
