from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  logout
# Create your views here.
from .models import *

@login_required
def dashboard(request):
    context  = {
        'nombre': "HOla"
    }
    return render(request, "app/index.html", context)

def landing(request):
    return render(request, "app/landing.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect('landing')

@login_required
def profile(request):
    perfil = request.user
    context = {
        'perfil': perfil,
    }
    return render(request, 'app/profile.html', context)

def about(request):
    return render(request, 'app/about.html')