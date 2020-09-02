from django.urls import path

from . import views

app_name = 'cakes'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
    path('cookies/', views.cookies, name='cookies'),
]