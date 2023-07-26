from .views import collector_view , CollectorView
from django.urls import path

urlpatterns = [
    path('', collector_view, name='getcollector'),
    path('add/', CollectorView.as_view(), name='addcollector')
]
