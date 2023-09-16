from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date
from cloudinary_storage.storage import  VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video


SEXO = [
    ('Macho', 'Macho'),
    ('Hembra', 'Hembra'),

]

CATEGORY = [
    ('Ganado Carne', 'Ganado Carne'),
    ('Ganado Lechero', 'Ganado Lechero'),
]

RACE = [
    ('Cebú', 'Cebú'),
    ('Simmental', 'Simmental'),
    ('Pardo Suizo', 'Pardo Suizo'),
    ('Jersey', 'Jersey'),
    ('Criollo', 'Criollo'),
    ('otro', 'otro'),

]

ESTADO = [
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo'),
    ('Vendido', 'Vendido'),
]

#PLAN = [
 #   ("Gratuito", "Gratuito"),
 #   ("Vip", "Vip"),
 #   ("Gold", "Gold"),
#]



class User(AbstractUser):

    def get_photo_url(self):
        if self.socialaccount_set.filter(provider='google'):
            return self.socialaccount_set.filter(provider='google')[0].extra_data['picture']
        else:
            return False
    
    def get_name(self):
        if self.socialaccount_set.filter(provider='google'):
            return self.socialaccount_set.filter(provider='google')[0].extra_data['name']
        else:
            return False

    def get_email(self):
        if self.socialaccount_set.filter(provider='google'):
            return self.socialaccount_set.filter(provider='google')[0].extra_data['email']
        else:
            return False
        
    pass


class UserInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length = 50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    #plan_precios = models.CharField(max_length=8, choices=PLAN, blank=True, null=True, default=None)
    cedula = models.CharField(max_length=100, null=True)
    # Diego el campo de la linea 74 es para que el administrador pueda verificar la cuenta del usuario vendedor
    is_verificado = models.BooleanField(null=True,blank=True, default=False)

    def __str__(self):
        return self.nombre 

class Ganaderia(models.Model):
    user_information = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
    nombre_ganaderia = models.CharField(max_length=50)  
    description = models.TextField(null=True, blank=True)
    lat = models.CharField(max_length = 50)
    lon = models.CharField(max_length = 50)

    def __str__(self):
        return self.nombre_ganaderia


class ProfileGanaderia(models.Model):
    publicacion = models.ForeignKey(Ganaderia, related_name='profile_ganado', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/vendetuvaca/profile/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class BovinoPublication(models.Model):
    ganaderia = models.ForeignKey(Ganaderia, related_name='Ganaderia', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    code = models.CharField(max_length=25)
    date_born = models.DateField()
    genero = models.CharField(max_length=7, choices=SEXO, default='Hembra')
    weight = models.DecimalField(max_digits=7, decimal_places=2)  
    race = models.CharField(max_length=25, choices=RACE, default='otro')
    categoria = models.CharField(max_length=15, choices=CATEGORY, default='Ganado Carne')
    estado = models.CharField(max_length=20, choices=ESTADO, default='Activo')


    def get_years(self):
        today = date.today()
        age_in_days = (today - self.date_born).days
        years = age_in_days // 365
        months = (age_in_days % 365) // 30

        if years > 0:
            if months > 0:
                return f"{years} años y {months} meses"
            return f"{years} años"
        elif months > 0:
            if months == 1:
                return f"{months} mes"
            return f"{months} meses"
        else:
            return f"{age_in_days} días"  

    def __str__(self):
        return f"{self.title}  /  {self.get_years()}"


class MultimediaImg(models.Model):
    publicacion = models.ForeignKey(BovinoPublication, related_name='imagen', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/vendetuvaca/publicacion/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class MultimediaVideo(models.Model):
    publicacion = models.ForeignKey(BovinoPublication, related_name='video', on_delete=models.CASCADE)
    video = models.ImageField(
        upload_to='images/vendetuvaca/videos/',  null=True,
        blank=True,  
        storage=VideoMediaCloudinaryStorage(),  
        validators=[validate_video] 
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)  

class MultimediaCertificadoInscripcion(models.Model):
    publicacion = models.ForeignKey(BovinoPublication, related_name='Incripcion', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/vendetuvaca/Inscripcion/', blank=True, null=True)


class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
