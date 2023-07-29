from django.urls import path
from .views import ListTeaTypes

urlpatterns = [
    path('', ListTeaTypes.as_view()),
]
