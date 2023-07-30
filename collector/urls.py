from .views import collector_view , CollectorView , GetCollectorByID
from django.urls import path

urlpatterns = [
    path('', collector_view, name='getcollector'),
    path('collector/', CollectorView.as_view(), name='addcollector'),
    path('getbyid/<int:id>', GetCollectorByID.as_view(), name='get collector by id'),
    
    
]
