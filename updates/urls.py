from . import views
from django.urls import path

urlpatterns = [
    path('', views.updates_view, name='getUpdates'),
]