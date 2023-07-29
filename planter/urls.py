from . import views
from django.urls import path
from .views import EstateNumberView , planter_view

urlpatterns = [
    path('', views.planter_view, name='getplanter'),
    path('<int:estate_id>/', EstateNumberView.as_view(), name='detail-by-estate_number'),
    path('planter/', views.planter_view, name='createplanter'),
]