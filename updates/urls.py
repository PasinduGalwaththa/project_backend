from . import views
from django.urls import path

urlpatterns = [
    path('', views.updates_view, name='getUpdates'),
    path('getbyidplanter/<int:planter_id>/', views.GetupdatesbyplanterId.as_view(), name='getUpdatesbyd'),
    path('getbyidcollector/<int:collector_id>/', views.GetupdatesbyCollectorId.as_view(), name='getUpdatesbyd'),
]