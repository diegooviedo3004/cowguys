from django.shortcuts import render, redirect 
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  logout
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import *

from .form import UserInformationForm, GanaderiaForm, ProfileGanaderiaForm

# Stripe
from django.conf import settings 
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


# Decorador
def require_no_information(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if UserInformation.objects.filter(user_id=request.user.id).exists():
            return redirect('profile')  
        return view_func(request, *args, **kwargs)
    return _wrapped_view



@login_required
def dashboard(request):
    context = {
        'ganados': MultimediaImg.objects.all(),
        "gold_users": UserInformation.objects.filter(plan_precios="Gold").exclude(user=request.user)
    }
    return render(request, "app/index.html", context=context)

def landing(request):
    return render(request, "app/landing.html")

@login_required
def profile(request):
    perfil = request.user

    # user_information = get_object_or_404(UserInformation, user = request.user)

    try:
        user_information = UserInformation.objects.get(user=request.user.id)
    except UserInformation.DoesNotExist: 
        user_information = None
    try:
        ganaderias_usuario = Ganaderia.objects.filter(user_information__user=request.user.id)
    except Ganaderia.DoesNotExist:
        ganaderias_usuario = None
    try:
        perfiles_de_ganaderia = ProfileGanaderia.objects.filter(publicacion__in=ganaderias_usuario)
    except:
        perfiles_de_ganaderia = None


    print(ganaderias_usuario)
    context = {
        'perfil': perfil,
        'userInformation': user_information,
        'ganados': ganaderias_usuario,
        'perfiles_de_ganaderia': perfiles_de_ganaderia,
    }
    return render(request, 'app/profile.html', context)

def about(request):
    return render(request, 'app/about.html')


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


@login_required 
def crearGanado(request):  
    if request.method == 'POST':
        ganaderia_form = GanaderiaForm(request.POST)
        profile_form = ProfileGanaderiaForm(request.POST, request.FILES)
        print(profile_form)
        if ganaderia_form.is_valid() and profile_form.is_valid():
            user_information = UserInformation.objects.get(user=request.user)
            ganaderia = ganaderia_form.save(commit=False)
            ganaderia.user_information = user_information
            ganaderia.save()
            # Save the ProfileGanaderia instance
            profile = profile_form.save(commit=False)
            profile.publicacion = ganaderia
            profile.save()
            response_data = {'success': True, 'message': 'Datos guardados con éxito'}
            return JsonResponse(response_data)
    else:
        form1 = GanaderiaForm()
        form2 = ProfileGanaderiaForm()

    context = {
        'form1': form1,
        'form2': form2,
    }
    return render(request, "app/crear_ganado.html", context)

@login_required
def perfil_ganaderia(request,pk):
    user_information = get_object_or_404(UserInformation, user=request.user)
    ganaderia = get_object_or_404(Ganaderia, id=pk)

    perfil_ganaderia = get_object_or_404(ProfileGanaderia, publicacion=ganaderia)

    bovinoPublication=BovinoPublication.objects.filter(ganaderia=ganaderia)

    context = {
        "userInformation": user_information,
        "ganaderia": ganaderia,
        "perfil_ganaderia": perfil_ganaderia,
        "bovinoPublication": bovinoPublication
    }
    return render(request, 'app/perfil_ganaderia.html', context)

def ganaderias(request):
    return render(request, 'app/ganaderias.html')

@login_required
def mensajes(request, user_id):
    pub_user = get_object_or_404(User, id=user_id)

    if pub_user == request.user:
        return HttpResponse("No puedes hablar contigo mismo")
    
    context = {
        "pub_user": pub_user,
        "user": request.user
    }
    return render(request, 'app/message.html', context)

@login_required
def crear_publicacion(request):
    form = UserInformationForm()

    context = {
        'form': form,
    }
    return render(request, 'app/crear_publicacion.html', context)


# Stripe
def checkout_view(request, pk):
    if request.method == "POST":
        try:
            product = Plan.objects.get(id=pk)
            YOUR_DOMAIN = settings.YOUR_DOMAIN
            checkout_session = stripe.checkout.Session.create(
                success_url=YOUR_DOMAIN + "/profile/",
                cancel_url=YOUR_DOMAIN + "/profile/",
                line_items=[
                    {
                        "price_data": {
                            "currency": 'usd',
                            "product_data": {
                                "name": product.name,
                            },
                            "unit_amount": product.price
                        },
                        "quantity": 1,
                    },
                ],
                metadata={
                    "product_id": product.id,
                    "user_id": request.user.id,
                    "quantity": 1
                },
                mode="payment",
            )
      
            return JsonResponse({
                'id': checkout_session.id
            })
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            })
    else:
        return redirect('profile')

@csrf_exempt
def my_webhook_view(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        event = stripe.Webhook.construct_event(
        payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

      # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        
        # Retrieve the session. If you require line items in the response, you may include them by expanding line_items.
        session = stripe.checkout.Session.retrieve(
            event['data']['object']['id'],
            expand=['line_items'],
        )
        product_id = session["metadata"]["product_id"]
        user_id = session["metadata"]["user_id"]

        user = User.objects.get(id=user_id)
        userinformation = UserInformation.objects.get(user=user)
        subscription = Plan.objects.get(id=product_id)
        userinformation.plan_precios = subscription.name
        userinformation.save()
      
    #line_items = session.line_items
    # Fulfill the purchase...
    #fulfill_order(line_items)

    # Passed signature verification
    return HttpResponse(status=200)

def plan(request):
    context = {
      "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'app/planes.html', context)