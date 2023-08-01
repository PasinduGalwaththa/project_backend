from .import views
from django.urls import path
from .views import paymentsView , GetListByPlanterId , PaymentsGetAmount , PaymentsGetWeigth
urlpatterns = [
    path('', paymentsView.as_view(), name='getpayments'),
    path('<int:pk>/', paymentsView.as_view(), name='updatepayments'),
    path('planter/<int:planter_id>/', GetListByPlanterId.as_view(), name='updatepayments'),
    path('getdata/amount' , PaymentsGetAmount.as_view() , name='getUpdatesbyd'),
    path('getdata/weight' , PaymentsGetWeigth.as_view() , name='getUpdatesbyd')
]
