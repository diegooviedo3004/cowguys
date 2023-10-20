from django.forms import ModelForm
from .models import UserInformation, Ganaderia, ProfileGanaderia

class UserInformationForm(ModelForm):
    class Meta:
        model = UserInformation
        fields =  ['telefono', 'nombre', 'apellido', 'cedula']

class GanaderiaForm(ModelForm):
    class Meta:
        model = Ganaderia
        fields = ['nombre_ganaderia', 'description', 'lat', 'lon']

class ProfileGanaderiaForm(ModelForm):
    class Meta:
        model = ProfileGanaderia
        fields = ['image']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        # Add your validation logic for the 'image' field here
        return image
