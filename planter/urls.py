from . import views
from django.urls import path

urlpatterns = [
    path('', views.planter_view, name='getplanter'),
    
]