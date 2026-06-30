from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.doctors_view, name='doctors'),
    
]