from django.urls import path
from . import views

#Andrade Chura Mary Carmen
app_name = 'encuesta'
urlpatterns = [
    #ex: /encuesta/
    path('', views.index, name='index'),
    path('enviar', views.enviar, name='enviar'),
]

