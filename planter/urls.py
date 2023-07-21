from . import views
from django.urls import path
from .views import EstateNumberView

urlpatterns = [
    path('', views.planter_view, name='getplanter'),
    path('<int:estatenumber>/', EstateNumberView.as_view(), name='detail-by-estate_number'),
    
    
]