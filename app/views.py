from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from .models import UserInformation, User
from .forms import UserInformationForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

# Create your views here.


def userinfo(request):
    if request.method == 'POST':
        form = UserInformationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Exito")
            return redirect('userinfo')
        else:
            print("Fatal")
            return render(request, 'userinfo.html', {'form': form})
    else:
        form = UserInformationForm()
        users = User.objects.all()
    return render(request, 'userinfo.html', {'form': form, 'users': users})

def crear_user_information(request):
    if request.method == 'POST':
        form = UserInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_user_information')
    else:
        form = UserInformationForm()
    
    return render(request, 'info.html', {'form': form})
