from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('customer/', views.customers, name="customers"),
    path('customer-trade-detail/<int:id>', views.customer_trade_detail, name="customer-trade-detail")
    
]
