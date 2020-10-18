from django.shortcuts import render
from django.http import HttpResponse    
from gestionPedidos.models import Articulos

# Create your views here.

def busqueda_productos(request):
    return render(request, 'busqueda_productos.html')

def buscar(request):

    if request.GET["prd"]:
        #mensaje='Articulo Buscado: %r' %request.GET["prd"]
        producto=request.GET['prd']
        if len(producto)>20:
            mensaje="El texto de busqueda es demasiado largo"
        else:
            articulos = Articulos.objects.filter(nombre__icontains=producto)

            return render(request,"resultados_busqueda.html", {"articulos":articulos, "query":producto})
    else:
        mensaje='No se ha introducido ningun valor'

    return HttpResponse(mensaje)