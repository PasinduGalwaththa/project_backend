from . import views
from django.urls import path
from .views import GetUpdatesWeightDate

urlpatterns = [
    path('', views.updates_view, name='getUpdates'),
    path('getbyidplanter/<int:planter_id>/', views.GetupdatesbyplanterId.as_view(), name='getUpdatesbyd'),
    path('getbyidcollector/<int:collector_id>/', views.GetupdatesbyCollectorId.as_view(), name='getUpdatesbyd'),
    path('getdata' , GetUpdatesWeightDate.as_view() , name='getUpdatesbyd')
]