from django.shortcuts import render
from cakes.models import Catergory, Cake

# Create your views here.
def index(request):
    return render(request, 'cakes/index.html', {
        "cakes": Cake.objects.all()
    })
