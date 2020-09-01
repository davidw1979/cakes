from django.contrib import admin

from cakes.models import Catergory, Cake

# Register your models here.
class CakeAdmin(admin.ModelAdmin):
    filter_horizontal = ("catergories",)

admin.site.register(Catergory)
admin.site.register(Cake, CakeAdmin)
