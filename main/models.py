# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Authorization(models.Model):
    license_plate = models.CharField(max_length=50)
    vehicle_name = models.CharField(max_length=50)
    make_model = models.CharField(max_length=50)
    vehicle_color = models.CharField(max_length=50)
    notes = models.CharField(max_length=50)
    is_authorized = models.IntegerField(null=True)

    def __str__(self):
        return self.vehicle_name

    def get_absolute_url(self):
        return reverse('vehicle_edit', kwargs={'pk':self.pk})