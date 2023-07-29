from .import views
from django.urls import path
from .views import paymentsView

urlpatterns = [
    path('', paymentsView.as_view(), name='getpayments'),
    path('<int:pk>/', paymentsView.as_view(), name='updatepayments'),
]
