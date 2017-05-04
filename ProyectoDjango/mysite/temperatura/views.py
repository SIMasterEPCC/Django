# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from temperatura.models import Temperatura
from temperatura.serializers import TemperaturaSerializer

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
 
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

    @csrf_exempt
	def temperatura_list(request):
	    if request.method == 'GET':
	        temperaturas = Temperatura.objects.all()
	        serializer = TemperaturaSerializer(temperaturas, many=True)
	        return JSONResponse(serializer.data)

	    elif request.method == 'POST':
	        data = JSONParser().parse(request)
	        serializer = TemperaturaSerializer(data=data)
	        if serializer.is_valid():
	            serializer.save()
	            return JSONResponse(serializer.data, status=201)
	        return JSONResponse(serializer.errors, status=400)