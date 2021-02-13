from django.urls import path
from ProyectoWebApps import views

urlpatterns = [
    path('',views.Home),
    path('Tienda/',views.Tienda),
    path('Servicios/',views.Servicios),
    path('Blog/',views.Blog),
    path('Contacto/',views.Contacto),
]
