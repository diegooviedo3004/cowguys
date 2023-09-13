from django import forms
from .models import UserInformation

class UserInformationForm(forms.ModelForm):
    class Meta:
        model = UserInformation
        fields = ['user' , 'telefono', 'nombre', 'apellido']
