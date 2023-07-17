from . import views
from django.urls import path
from set_arrivals.views import DetailByDayView


urlpatterns = [
    path('', views.SetArrivals_view, name='getUpdates'),
    path('<str:day>/', DetailByDayView.as_view(), name='detail-by-day'),
    
    path('delete/<int:pk>/', views.SetArrivals_view, name='delete-contact'),
    path('update/<int:pk>/', views.SetArrivals_view, name='update-contact'),
    ]