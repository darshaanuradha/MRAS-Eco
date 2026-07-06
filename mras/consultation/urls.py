from django.urls import path
from . import views

urlpatterns = [
    path('', views.ConsultationListView.as_view(), name='consultation_list'),
    path('new/', views.ConsultationCreateView.as_view(), name='consultation_create'),
    path('<int:pk>/edit/', views.ConsultationUpdateView.as_view(), name='consultation_edit'),
    path('<int:pk>/print/', views.ConsultationPrintView.as_view(), name='consultation_print'),
    
]