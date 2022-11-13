
from django.contrib import admin
from django.urls import path
from list_task import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('signup/', views.signupuser, name ='signupuser'),
    path('login/', views.loginuser, name ='loginuser'),
    path('logout/', views.logoutuser, name ='logoutuser'),
    
    path('', views.home, name ='home'),
    path('create/', views.createtodo, name='createtodo'),
    path('current/', views.currenttodos, name ='currenttodos'),
    ]
