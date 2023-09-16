from django.forms import ModelForm
from .models import UserInformation

class UserInformationForm(ModelForm):
    class Meta:
        model = UserInformation
        fields =  ['telefono', 'nombre', 'apellido', 'cedula']
