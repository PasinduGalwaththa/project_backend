from .import views
from django.urls import path
from .views import paymentsrView

urlpatterns = [
    path('<int:estatenumber>/', views.payments_view, name='getpayments'),
]
