from . import views
from django.urls import path
from .views import EstateNumberView , planter_view , PlanterIDview , AddPlanterView , AddPlanter , PlanterDetail


urlpatterns = [
    path('', AddPlanter.as_view(), name='getplanter'),
    path('<int:estate_id>/', EstateNumberView.as_view(), name='detail-by-estate_number'),
    path('planter/', views.planter_view, name='createplanter'),
    path('id/<int:id>/', PlanterIDview.as_view(), name='detail-by-planter_id'),
    path('add_planter/', AddPlanterView.as_view(), name='add_planter'),
    path('add/', PlanterDetail.as_view(), name='planter_detail'),
    
]