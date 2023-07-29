from . import views
from django.urls import path

urlpatterns = [
    path('', views.updates_view, name='getUpdates'),
    path('getbyid/<int:planter_id>/', views.Getupdatesbyd.as_view(), name='getUpdatesbyd'),
]