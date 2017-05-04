import datetime
from django.shortcuts import render_to_response
from os import listdir
from django.template import Template, Context
from django.http import HttpResponse
from temperatura.models import Temperatura


def listadoTemperaturas(request):
    now = datetime.datetime.now()
    fp = open('templates/current_datetime.html')
    t = Template(fp.read())
    fp.close()

    #p = Temperatura(humedad='34', direccion='45')
    #p.save()

    var = Temperatura.objects.all()


    html = t.render(Context({'current_date': var}))
    return HttpResponse(html)

'''
def temperatura_list(request):
    temperaturas = Book.objects.order_by('name')
    fp = open('templates/current_datetime.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context({'current_date': temperaturas}))
    return HttpResponse(html) 
'''