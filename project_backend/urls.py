from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import path , include
# from django.views.generic import planter_view




urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('updates/' , include('updates.urls')),
    path('planter/' , include('planter.urls')),
    path('setarrivals/',include('set_arrivals.urls')),
    path('collector/',include('collector.urls')),
    path('estate/',include('estate.urls')),
    path('user/' , include('user.urls')),
    path('route/', include('route.urls')),
    path('payments/', include('payements.urls')),
    path('teatype/', include('teatype.urls')),
    
   
]
