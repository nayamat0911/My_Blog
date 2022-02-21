
from django.urls import path
from .import views

app_name='login_app'

urlpatterns = [
    path('', views.User_login, name='User_login'),
    path('signup/', views.SignUp, name='SignUp'),
    path('logout/', views.User_logout, name='User_logout'),
    path('profile/', views.User_profile, name='User_profile'),
    path('edit_profile/', views.User_change, name='User_change'),
    path('password/', views.pass_change, name='pass_change'),
    path('add_pro/', views.add_pro_pic, name='add_pro_pic'),
    path('change_pro/', views.change_pic, name='change_pic'),
    
]
