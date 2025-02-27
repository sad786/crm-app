from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customer/add/', views.add_customer, name='add_customer'),
    path('customer/<int:customer_id>/add_interaction/', views.add_interaction, name='add_interaction'),
    path('customer/<int:customer_id>/add_note/', views.add_note, name='add_note'),
]