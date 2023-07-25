from . import views
from django.urls import path
from .views import estateView

urlpatterns = [
    path('', estateView.as_view(), name='getestate'),
]