from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_view, name='inventory'),
    path('medicine/add/', views.add_medicine, name='add_medicine'),
    path('medicine/edit/<int:pk>/', views.edit_medicine, name='edit_medicine'),
    path('medicine/delete/<int:pk>/', views.delete_medicine, name='delete_medicine'),
    path('stock/add/', views.add_inventory, name='add_inventory'),
    path('stock/view/<int:pk>/', views.stock_view, name='stock_view'),
]