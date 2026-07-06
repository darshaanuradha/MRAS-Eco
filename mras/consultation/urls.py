from django.urls import path
from . import views

urlpatterns = [
    # path('', views.consultation_view, name='consultation'),
    path('', views.ConsultationListView.as_view(), name='consultation_list'),
    path('new/', views.ConsultationCreateView.as_view(), name='consultation_create'),
    path('<int:pk>/edit/', views.ConsultationUpdateView.as_view(), name='consultation_edit'),
    
]