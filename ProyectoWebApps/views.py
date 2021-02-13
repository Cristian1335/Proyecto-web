from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home(request):
    return render(request, "ProyectoWebApp/Home.html")

def Servicios(request):
    return render(request, "ProyectoWebApp/Servicios.html")

def Tienda(request):
    return render(request, "ProyectoWebApp/Tienda.html")

def Blog(request):
    return render(request, "ProyectoWebApp/Blog.html")

def Contacto(request):
    return render(request, "ProyectoWebApp/Contacto.html")