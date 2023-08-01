from . import views
from django.urls import path
from .views import estateView , AddStateView , EstateIdOnlyView

urlpatterns = [
    path('', estateView.as_view(), name='getestate'),
    path('getnymbers/', EstateIdOnlyView.as_view(), name='getestatenumber'),
]