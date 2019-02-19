"""parkpow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from main import views as v
from django.conf.urls.static import static

urlpatterns = [    
    path('', v.base, name='base'),
    path('dashboard/', v.dashboard, name='demo_dashboard'),
    path('vehicle/', v.vehicle, name='demo_vehicle'),
    path('alert/', v.alert, name='demo_alert'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path('authorization/', v.vehicleView, name='demo_authorization'),
    path('authorization/vehicle_new/<str:auth_flag>', v.vehicleNew, name='vehicle_new'),
    path('authorization/vehicle_view', v.vehicleView, name='vehicle_view'),
    path('authorization/vehicle_delete/<int:vehicle_id>/<str:auth_flag>', v.vehicleDelete, name='vehicle_delete'),
    path('authorization/vehicle_edit/<int:vehicle_id>/<str:auth_flag>', v.vehicleEdit, name='vehicle_edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)
