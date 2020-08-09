from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("<h1>Proyecto <h1>");

def inicio(request, template="inicio.html"):
    return render(request,template);

def Login(request):
    return HttpResponse("<h1>Proyecto <h1>");


def acerca_de(request, template="acerca_de.html"):
    return render(request,template);

def contacto(request, template="contacto.html"):
    return render(request,template);

def productos(request, template="productos.html"):
    return render(request,template);