# urls.py
from django.urls import path
from .views import RouteListCreateView, RouteRetrieveUpdateDestroyView , RouteDetailsListCreateView

urlpatterns = [
    path('routes/', RouteListCreateView.as_view(), name='route-list-create'),
    path('routes/<int:pk>/', RouteRetrieveUpdateDestroyView.as_view(), name='route-retrieve-update-destroy'),
    path('routesdetails/', RouteDetailsListCreateView.as_view(), name='routeupdate'),
]
