from .models import ActivoFijo
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

def ActivoFijoList(request):
    queryset = ActivoFijo.objects.all()
    context = list(queryset.values('id', 'name'))
    return JsonResponse(context, safe=False)

def ActivoFijoCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        activofijo = ActivoFijo()
        activofijo.name = data_json["name"]
        activofijo.save()
        return HttpResponse("successfully created activofijo")