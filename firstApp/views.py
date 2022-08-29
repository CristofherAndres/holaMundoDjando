from django.shortcuts import render
from django.http import HttpResponse
import datetime

#Crear nuestra primera vista en Python
# Nos mostrara un Hola Mundo
def display(request):
    return HttpResponse("<h1>Hola Mundo Cristofher!!</h1>")

#Segunda vista en nuestra APP
def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b>Fecha y Hora actual: </b>" +str(dt)
    return HttpResponse(s)
    

#CReamos 3ra vista
def displayButton(request):
    b = "<button>Enviar!!</button>"
    return HttpResponse(b)