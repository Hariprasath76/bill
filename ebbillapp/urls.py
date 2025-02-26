from django.urls import path
from ebbillapp import views

urlpatterns = [
    path('',views.ebCalculation,name='dashboard'),
    # path('index',views.ebCalculation,name='index'),
    # path('checkDetails',views.checkDetails,name='checkDetails'),
    
]