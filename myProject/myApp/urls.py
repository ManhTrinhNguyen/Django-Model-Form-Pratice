from django.urls import path 
from .views import view_customer_form, view_order_form

urlpatterns = [
  path('customer/', view_customer_form),
  path('order/', view_order_form)
]

