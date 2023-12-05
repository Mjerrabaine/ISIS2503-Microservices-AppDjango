from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views
#urls
urlpatterns = [
    url(r'^hospitales/', views.HospitalList),
    url(r'^hospitalcreate/$', csrf_exempt(views.HospitalCreate), name='hospitalCreate'),
    url(r'^createhospitales/$', csrf_exempt(views.HospitalesCreate), name='createHospitales'),
]