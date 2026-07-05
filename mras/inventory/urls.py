from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_view, name='inventory'),
    path('inventory/add/', views.add_medicine, name='add_medicine'),
    path('inventory/edit/<int:pk>/', views.edit_medicine, name='edit_medicine'),
    path('inventory/delete/<int:pk>/', views.delete_medicine, name='delete_medicine'),
]