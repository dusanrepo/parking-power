from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView

from authorization.models import Authorization

# Create your views here.

class VehicleList(ListView):
    model = Authorization

class AuthorizationCreate(ListView):
    model = Authorization
    success_url = reverse_lazy('')

class AuthorizationView(ListView):
    model = Authorization
    success_url = reverse_lazy('authorization')

class AuthorizationUpdate(ListView):
    model = Authorization
    success_url = reverse_lazy('authorization')

class AuthorizationDelete(ListView):
    model = Authorization
    success_url = reverse_lazy('authorization')
    