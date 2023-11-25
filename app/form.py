from django.forms import ModelForm
from .models import UserInformation, Ganaderia, ProfileGanaderia, BovinoPublication


class BovinoPublicationForm(ModelForm):
    #def _init_(self, current_user, *args, **kwargs):
        #super(BovinoPublicationForm, self)._init_(*args, **kwargs)
        #self.fields['ganaderia'].queryset = self.fields['ganaderia'].queryset.filter(ganaderia__user_information__user=current_user)

    class Meta:
        model = BovinoPublication
        fields = ['title', 'description', 'code', 'date_born', 'weight', 'race', 'categoria', 'price' ]
        exclude = ("estado",)


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
