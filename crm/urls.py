from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('customer/delete/<int:customer_id>/',views.delete,name='delete'),
    path('customer_list/',views.customer_list,name='customer_list'),
    path('logout/',LogoutView.as_view(next_page='customer_list'),name='logout'),
    path('', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customer/add/', views.add_customer, name='add_customer'),
    path('customer/<int:customer_id>/add_interaction/', views.add_interaction, name='add_interaction'),
    path('customer/<int:customer_id>/add_note/', views.add_note, name='add_note'),
]