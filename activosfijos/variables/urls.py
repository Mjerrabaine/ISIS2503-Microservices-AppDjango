from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^activosfijos/', views.ActivoFijoList, name='activofijoList'),
    url(r'^activofijocreate/$', csrf_exempt(views.ActivoFijoCreate), name='activofijoCreate'),
]