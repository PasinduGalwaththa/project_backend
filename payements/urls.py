from .import views
from django.urls import path
from .views import paymentsView , GetListByPlanterId

urlpatterns = [
    path('', paymentsView.as_view(), name='getpayments'),
    path('<int:pk>/', paymentsView.as_view(), name='updatepayments'),
    path('planter/<int:planter_id>/', GetListByPlanterId.as_view(), name='updatepayments'),
]
