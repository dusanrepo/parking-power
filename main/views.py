# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import datetime, timedelta
from random import randint, seed
from django.shortcuts import render, redirect, get_object_or_404

from main.models import Authorization

def base(request):
    return render(request, 'demo/base.html')

def dashboard(request):
    return render(request, 'demo/dashboard.html', dict(menu='dashboard'))


def vehicle(request):
    return render(request, 'demo/vehicle.html', dict(now=datetime.now(), menu='vehicle'))


def alert(request):
    # fake.seed(1)
    # seed(1)

    # def fake_alert():
    #     return fake.word([
    #         'Blacklisted vehicle has arrived',
    #         'Unapproved vehicle parked for 1h',
    #         'Vehicle parked for 1h',
    #         'Vehicle parked for 3h',
    #         'Unapproved vehicle parked for 3h'])

    # Alerts
    # alerts = []
    # date = datetime.now()
    # for _ in range(8):
    #     alerts.append(dict(
    #         date=date,
    #         value=fake.license_plate(),
    #         approved=randint(0, 2) == 1,
    #         note=fake_alert()))
    #     date -= timedelta(days=2) + timedelta(minutes=87)

    # Templates
    # templates = []
    # for _ in range(5):
    #     templates.append(dict(emails="%s, %s" % (fake.email(), fake.email()),
    #                           phone_nums=fake.phone_number(), type=fake_alert()))
    return render(request, 'demo/alert.html', dict(alerts=alerts, templates=templates, menu='alert'))


def vehicleView(request):
    # fake.seed(1)
    # whitelist = []
    # blacklist = []
    # for i in range(7):
    #     whitelist.append(dict(value=fake.license_plate(), name=fake.name(),
    #                           make=fake_model(), color=fake.safe_color_name(), notes=''))
    # for i in range(5):
    #     blacklist.append(dict(value=fake.license_plate(), name=fake.name(),
    #                           make=fake_model(), color=fake.safe_color_name(), notes=''))
    vehicles = Authorization.objects.all()
    data = {}
    data['whitelist'] = vehicles.filter(is_authorized = "1")
    data['blacklist'] = vehicles.filter(is_authorized = "-1")
    return render(request, 'demo/authorization.html', data)

def vehicleNew(request, auth_flag):
    if request.method == "POST":

        license_plate = request.POST.get("license_plate", "")
        vehicle_name = request.POST.get("vehicle_name", "")
        vehicle_model_make = request.POST.get("vehicle_model_make", "")
        vehicle_color = request.POST.get("vehicle_color", "")
        vehicle_note = request.POST.get("vehicle_note", "")
        
        new_vehicle = Authorization(license_plate=license_plate, vehicle_name=vehicle_name, make_model=vehicle_model_make, vehicle_color=vehicle_color, notes=vehicle_note, is_authorized=auth_flag)
        
        new_vehicle.save()
    return redirect('vehicle_view')
    # vehicles = Authorization.objects.all()
    # data = {}
    # data['whitelist'] = vehicles.filter(is_authorized = "1")
    # data['blacklist'] = vehicles.filter(is_authorized = "-1")

    # return render(request, 'demo/authorization.html', data)

def vehicleDelete(request, vehicle_id, auth_flag):
    
    selected = get_object_or_404(Authorization, id=vehicle_id, is_authorized=auth_flag)
    print(vehicle_id)
    print(selected)
    if request.method == "POST":
        selected.delete()
        print(selected)
        return redirect('vehicle_view')
    return render(request, 'demo/authorization.html', data)

def vehicleEdit(request, vehicle_id, auth_flag):
    selected = get_object_or_404(Authorization, id=vehicle_id, is_authorized=auth_flag)
    print(selected)
    if request.method == "POST":
        license_plate = request.POST.get("license_plate", "")
        vehicle_name = request.POST.get("vehicle_name", "")
        vehicle_model_make = request.POST.get("vehicle_model_make", "")
        vehicle_color = request.POST.get("vehicle_color", "")
        vehicle_note = request.POST.get("vehicle_note", "")
        
        updated = Authorization(license_plate=license_plate, vehicle_name=vehicle_name, make_model=vehicle_model_make, vehicle_color=vehicle_color, notes=vehicle_note, is_authorized=auth_flag)
        updated.save()
        selected.delete()
        print(updated)
        
    return redirect('vehicle_view')