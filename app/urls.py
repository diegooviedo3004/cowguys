from . import views
from django.urls import path

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('landing/', views.landing, name="landing"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('about/', views.about, name="about"),
    path('crear_info/', views.crearInfo, name='crearinfo'),
    path('planes/', views.plan, name='planespago'),
]