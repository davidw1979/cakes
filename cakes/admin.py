from django.contrib import admin

# Register your models here.
from cakes.models import Catergory, Cake

admin.site.register(Catergory)
admin.site.register(Cake)
