from .models import Cita
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

def CitaList(request):
    queryset = Cita.objects.all()
    context = list(queryset.values('id', 'name'))
    return JsonResponse(context, safe=False)

def CitaCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        cita = Cita()
        cita.name = data_json["name"]
        cita.save()
        return HttpResponse("successfully created cita")