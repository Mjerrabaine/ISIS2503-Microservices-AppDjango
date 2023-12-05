from .models import Hospital
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json

def check_variable(data):
    r = requests.get(settings.PATH_VAR, headers={"Accept":"application/json"})
    variables = r.json()
    for variable in variables:
        if data["variable"] == variable["id"]:
            return True
    return False

def HospitalList(request):
    queryset = Hospital.objects.all()
    context = list(queryset.values('id', 'variable', 'value', 'unit', 'place', 'dateTime'))
    return JsonResponse(context, safe=False)

def HospitalCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_variable(data_json) == True:
            hospital = Hospital()
            hospital.variable = data_json['variable']
            hospital.value = data_json['value']
            hospital.unit = data_json['unit']
            hospital.place = data_json['place']
            hospital.save()
            return HttpResponse("successfully created hospital")
        else:
            return HttpResponse("unsuccessfully created hospital. Variable does not exist")

def HospitalsCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        hospital_list = []
        for hospital in data_json:
                    if check_variable(hospital) == True:
                        db_hospital = Hospital()
                        db_hospital.variable = hospital['variable']
                        db_hospital.value = hospital['value']
                        db_hospital.unit = hospital['unit']
                        db_hospital.place = hospital['place']
                        hospital_list.append(db_hospital)
                    else:
                        return HttpResponse("unsuccessfully created hospital. Variable does not exist")
        
        Hospital.objects.bulk_create(hospital_list)
        return HttpResponse("successfully created hospitals")