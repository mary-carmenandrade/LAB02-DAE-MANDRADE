from django.urls import path
from . import views

#Andrade Chura Mary Carmen
app_name = 'volumen'
urlpatterns = [
    #ex: /cvolumen/
    path('', views.index, name='index'),
    path('calcular', views.calcular, name='calcular'),
]
