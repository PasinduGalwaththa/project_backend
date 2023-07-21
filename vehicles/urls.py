from .import views
from django.urls import path

urlpatterns = [
    path('', views.vehicles_view, name='getVehicles'),
]
