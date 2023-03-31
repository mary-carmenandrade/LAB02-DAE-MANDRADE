from django.shortcuts import render
from django.http import HttpResponse

# Andrade Chura Mary Carmen
def index(request):
    context = {
        'titulo': "Formulario2",
    }
    return render(request, 'calculadora/formulario2.html', context)

def calcular(request):
    
    titulo = "Resultado"
    operacion = request.POST['operacion']
    num1 = float(request.POST['num1'])
    num2 = float(request.POST['num2'])
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    
    return render(request, 'calculadora/resultado.html', {'titulo': titulo, 'operacion': operacion, 
    'num1': num1, 'num2': num2, 'suma': suma, 'resta': resta, 'multiplicacion': multiplicacion, 'division': division})