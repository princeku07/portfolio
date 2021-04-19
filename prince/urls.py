from django.contrib import admin
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path,re_path,include
from .views import *
from . import views

admin.site.header = "BeHealthy"
urlpatterns = [
    path('',HomeView.as_view(), name ='home'),
    # path('home',views.home ,name='home'),
    path('home',HomeView.as_view(), name='home'),
    path('contact',views.contact, name ='contact'),
    path('blog',PostListView.as_view(), name='blog'),
    path('blog/<int:pk>',PostDetailView.as_view(), name ='post-detail'),
    path('category/<str:cats>/',CategoryView,name='category'),
    path('about',views.about, name ='about'),
    path('project',views.project, name ='project'),    
    
    ]