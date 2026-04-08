import os
from django import get_version
from django.conf import settings
from django.shortcuts import render

class Empresa:
    def __init__(self, nombre, sector):
        self.nombre = nombre
        self.sector = sector

class Campana:
    def __init__(self, objeto_empresa, presupuesto):
        self.empresa = objeto_empresa  
        self.presupuesto = presupuesto
        self.estado = "Protegido (Escrow)"

def home(request):
    mi_empresa = Empresa("Sebastian Corp", "Tecnología y Marketing")
    mi_proyecto = Campana(mi_empresa, 500)

    context = {"django_version": "Django 6.0.2 CAMBIOS", 
        "python_version": "Python 3.14.2 MAS CAMBIOS",
        "proyecto": mi_proyecto  }

    return render(request, 'pages/home.html', context)

