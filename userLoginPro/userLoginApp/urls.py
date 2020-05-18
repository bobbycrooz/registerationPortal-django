from django.urls import path
from django.contrib import admin
from userLoginApp import views
#template tagging
app_name = 'websites'

#patterns
urlpatterns = [
    path('home/',views.index, name='home' ),
    path('register/', views.register, name='signup'),
    path('login/',views.userLogin, name='userlogin'),
    path('', views.serverOK, name='severOK'),
    path('logout/', views.logout_success, name='logout'),
]
