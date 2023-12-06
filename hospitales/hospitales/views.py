from .models import Hospital
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json

def check_activofijo(data):
    r = requests.get(settings.PATH_VAR, headers={"Accept":"application/json"})
    variables = r.json()
    for variable in variables:
        if data["activofijo"] == variable["id"]:
            return True
    return False

def HospitalList(request):
    queryset = Hospital.objects.all()
    context = list(queryset.values('id', 'activofijo', 'precio', 'marca', 'numquejas', 'dateTime'))
    return JsonResponse(context, safe=False)

def HospitalCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_activofijo(data_json) == True:
            hospital = Hospital()
            hospital.activofijo = data_json['activofijo']
            hospital.precio = data_json['precio']
            hospital.marca = data_json['marca']
            hospital.numquejas = data_json['numquejas']
            hospital.save()
            return HttpResponse("successfully created hospital")
        else:
            return HttpResponse("unsuccessfully created hospital. ActivoFijo does not exist")

def HospitalesCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        hospital_list = []
        for hospital in data_json:
                    if check_activofijo(hospital) == True:
                        db_hospital = Hospital()
                        db_hospital.activofijo = hospital['activofijo']
                        db_hospital.precio = hospital['precio']
                        db_hospital.unit = hospital['unit']
                        db_hospital.numquejas = hospital['numquejas']
                        hospital_list.append(db_hospital)
                    else:
                        return HttpResponse("unsuccessfully created hospital. ActivoFijo does not exist")
        
        Hospital.objects.bulk_create(hospital_list)
        return HttpResponse("successfully created hospital")