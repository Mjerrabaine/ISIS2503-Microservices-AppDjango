from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^hospitales/', views.HospitalList),
    url(r'^hospitalcreate/$', csrf_exempt(views.HospitalCreate), name='hospitalCreate'),
    url(r'^createhospitals/$', csrf_exempt(views.HospitalsCreate), name='createHospitals'),
]