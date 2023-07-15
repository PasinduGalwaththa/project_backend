
from django.contrib import admin
from django.urls import path , include
# from django.views.generic import planter_view




urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('updates/' , include('updates.urls')),
    path('planter/' , include('planter.urls')),
    path('setarrivals/',include('set_arrivals.urls')),
   
]
