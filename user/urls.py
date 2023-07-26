from django.urls import path
from .views import MyTokenObtainPairView , UserView

#http://127.0.0.1:8000/user/......

urlpatterns = [
    path('token' , MyTokenObtainPairView.as_view() , name = "login"),
    path('' , UserView.as_view() , name = "user")
]
