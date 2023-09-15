from django.shortcuts import render, redirect 
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  logout
# Create your views here.
from .models import *

from .form import UserInformationForm



# Decorador
def require_no_information(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if UserInformation.objects.filter(user_id=request.user.id).exists():
            return redirect('profile')  
        return view_func(request, *args, **kwargs)
    return _wrapped_view


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
    try:
        user_information = UserInformation.objects.get(user=request.user)
        ganaderias_del_usuario = []
    except UserInformation.DoesNotExist:
       
        user_information = None
        ganaderias_del_usuario = []

    context = {
        'perfil': perfil,
        'userInformation': user_information,
        'ganados': ganaderias_del_usuario,
    }
    return render(request, 'app/profile.html', context)

def about(request):
    return render(request, 'app/about.html')
from django.shortcuts import render, redirect

@login_required 
@require_no_information 
def crearInfo(request):
    if request.method == "POST":
        form = UserInformationForm(request.POST)
        if form.is_valid():
            telefono = form.cleaned_data['telefono']
            cedula = form.cleaned_data['cedula']

            if UserInformation.objects.filter(telefono=telefono).exists():
                response_data = {'success': False, 'errors': {'telefono': 'Este número de teléfono ya está en uso por otro usuario.'}}
            
            elif UserInformation.objects.filter(cedula=cedula).exists():
                response_data = {'success': False, 'errors': {'telefono': 'Su cedula ya tiene una cuenta sociada.'}}

            else:
                user_info = form.save(commit=False)
                user_info.user_id = request.user.id
                user_info.save()
                response_data = {'success': True, 'message': 'Datos guardados con éxito'}
        else:
            errors = form.errors
            response_data = {'success': False, 'errors': errors}
        return JsonResponse(response_data)
    else:
        form = UserInformationForm()

    context = {
        'form': form,
    }
    return render(request, "app/crear_informacion.html", context)


def plan(request):
    return render(request, 'app/planes.html')