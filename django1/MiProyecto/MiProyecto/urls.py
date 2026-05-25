"""
URL configuration for MiProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from cursos.views import mostrarForm
#from cursos.views import cursos

def holamundo(request):
    print (request.headers)
    return HttpResponse('<h1>Hola mundo desde django</h1>')

def saludo(request):
    nombre = request.GET['nombre']
    return HttpResponse('<center>Hola'+nombre+'</center>')

def suma(request,n1,n2):
    resultado = n1+n2
    return HttpResponse('El resultado es: '+ str(resultado))

def calculadora(request,n1,n2,operacion):
    if operacion == 'suma':
        resultado = n1+n2
    elif operacion == 'resta':
        resultado = n1-n2
    else:
        resultado = 'operación no válida'
    return HttpResponse('El resultado es: '+ str(resultado))


urlpatterns = [
    path('holamundo/',holamundo),
    path('admin/', admin.site.urls),
    path('saludo/',saludo),
    path('suma/<int:n1>/<int:n2>',suma),
    path('calculadora/<int:n1>/<int:n2>/<str:operacion>',calculadora),
    path('formulario/',mostrarForm)
]
