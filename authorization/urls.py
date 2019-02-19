from django.urls import path
from authorization import views

urlpatterns = [
    path('', views.VehicleList.as_view(), name='vehicle_list'),
    path('new/', views.AuthorizationCreate.as_view(), name='vehicle_new'),
    path('edit/<int:pk>', views.AuthorizationUpdate.as_view(), name='vehicle_edit'),
    path('delete/<int:pk>', views.AuthorizationDelete.as_view(), name='vehicle_delete'),
    path('view/', views.AuthorizationView.as_view(), name='vehicle_view'),
]