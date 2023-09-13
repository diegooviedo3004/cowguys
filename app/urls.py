from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("userinfo/", views.userinfo, name="userinfo"),
    path('crear_user_information/', views.crear_user_information, name='crear_user_information'),

]