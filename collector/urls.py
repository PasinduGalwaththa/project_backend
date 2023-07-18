from .import views
from django.urls import path

urlpatterns = [
    path('', views.collector_view, name='getcollector'),
]
