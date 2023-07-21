from . import views
from django.urls import path
from l.views import estateView

urlpatterns = [
    path('', views.estate_view, name='getestate'),
]