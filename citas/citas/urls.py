from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^citas/', views.citaList, name='citaList'),
    url(r'^citacreate/$', csrf_exempt(views.citaCreate), name='citaCreate'),
]