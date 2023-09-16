from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(UserInformation)
admin.site.register(Ganaderia)
admin.site.register(ProfileGanaderia)
admin.site.register(BovinoPublication)
admin.site.register(MultimediaImg)
admin.site.register(MultimediaVideo)
admin.site.register(Plan)
