from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('', views.patient_list, name='list'),
    path('new/', views.patient_create, name='create'),
    path('<int:pk>/edit/', views.patient_update, name='edit'),
    path('<int:pk>/delete/', views.patient_delete, name='delete'),
]