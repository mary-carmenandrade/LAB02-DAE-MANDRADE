from django.shortcuts import render
from django.http import HttpResponse
from cmath import pi

# Andrade Chura Mary Carmen
def index(request):
    context = {
        'titulo': "Volumen de un Cilindro",
    }
    return render(request, 'volumen/formulario3.html', context)

def calcular(request):
    
    titulo = "Resultado"
    diametro = float(request.POST['diametro'])
    altura = float(request.POST['altura'])
    radio = diametro/2
    volumen = (radio**2)*pi*altura 
    return render(request, 'volumen/resultado.html', {'titulo': titulo, 
    'volumen': volumen, 'diametro': diametro, 'altura': altura})

    