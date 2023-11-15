from . import views
from django.urls import path

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('', views.landing, name="landing"),
    path('profile/', views.profile, name="profile"),
    path('about/', views.about, name="about"),
    path('crear_info/', views.crearInfo, name='crearinfo'),
    path('planes/', views.plan, name='planespago'),
    path('crear/ganado/', views.crearGanado, name="crear-ganado"),
    path('ganaderias/', views.ganaderias, name="ganaderias"),
    path('mensajes/<int:user_id>', views.mensajes, name="mensajes"),
    path('publicacion/<pk>', views.ver_publicaciones, name="ver-publicaciones"),

    path("perfil/ganaderia/<pk>/", views.perfil_ganaderia, name="perfil_ganaderia"),
    path("crear/publicacion/", views.crear_publicacion, name="crear_publicacion"),
    path("mapa/", views.map_nicaragua, name="map_nicaragua"),

    # Stripe
    path('checkout-session/<pk>/', views.checkout_view, name="create-checkout-session"),
    path('webhooks/stripe/', views.my_webhook_view, name="stripe-webhook"),
    

]