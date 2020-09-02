from django.shortcuts import render
from cakes.models import Catergory, Cake

# Create your views here.
def index(request):
    context = {'hero_present': 'hero-present'}
    return render(request, 'cakes/index.html', context)


def contact(request):
    context = {'no_hero': 'no-hero'}
    return render(request, 'cakes/contact.html', context)


def products(request):
    context = {
        'no_hero': 'no-hero',
        'cakes': Cake.objects.all()
        }
    return render(request, 'cakes/products.html', context)


def cookies(request):
    context = {'no_hero': 'no-hero'}
    return render(request, 'cakes/cookies.html', context)