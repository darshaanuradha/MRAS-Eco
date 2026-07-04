from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_list, name='patients'),
    path('<int:pk>/', views.patient_detail, name='patient_detail'),
]