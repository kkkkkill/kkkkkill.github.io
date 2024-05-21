"""BookSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from BookApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #用户注册
    path('register/', views.RegisterView.as_view()),
    #用户登录
    path('login/', views.LoginView.as_view()),
    #响应验证码
    path('image/', views.CodeImg),
    #响应首页
    path('index/', views.index),
    #响应出版社列表页
    path('publisher_list/', views.publisher_list),
    #添加出版社信息
    path('publisher_add/', views.publisher_add),
    #删除出版社信息
    path('publisher_del/', views.publisher_del),
    #修改出版社信息
    path('edit/', views.EditPublisher.as_view()),
    #响应图书信息
    path('book_list/', views.book_list),
    #添加图书信息
    path('book_add/', views.book_add),
    #删除图书信息
    path('book_del/', views.book_del),
    #修改图书信息
    path('book_edit/', views.EditBook.as_view()),
    #响应作者信息
    path('author_list/', views.author_list),
    #添加作者信息
    path('author_add/', views.AddAuthor.as_view()),
    #查看作品
    path('check_author/', views.check_author),
    #删除作者信息
    path('author_del/', views.author_del),
    #修改作者信息
    path('author_edit/', views.EditAuthor.as_view()),

    re_path('count/(?P<username>[A-Za-z0-9_]{3,15})/', views.UsernameCount)
]
