from django.urls import path
from . import views

urlpatterns = [
    path('', views.consultation_view, name='consultation'),
    
]