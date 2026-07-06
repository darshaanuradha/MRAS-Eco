from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import ListView, CreateView, UpdateView
from .models import Consultation
from .forms import ConsultationForm, PrescriptionFormSet

class ConsultationListView(ListView):
    model = Consultation
    template_name = 'consultation_list.html'
    context_object_name = 'consultations'
    
    def get_queryset(self):
        return Consultation.objects.select_related('patient', 'doctor').all()

class ConsultationCreateView(CreateView):
    model = Consultation
    form_class = ConsultationForm
    template_name = 'consultation_form.html'
    success_url = reverse_lazy('consultation_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['prescriptions'] = PrescriptionFormSet(self.request.POST)
        else:
            data['prescriptions'] = PrescriptionFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        prescriptions = context['prescriptions']
        
        with transaction.atomic():
            self.object = form.save()
            if prescriptions.is_valid():
                prescriptions.instance = self.object
                prescriptions.save()
            else:
                return self.form_invalid(form)
                
        return super().form_valid(form)

class ConsultationUpdateView(UpdateView):
    model = Consultation
    form_class = ConsultationForm
    template_name = 'consultation_form.html'
    success_url = reverse_lazy('consultation_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['prescriptions'] = PrescriptionFormSet(self.request.POST, instance=self.object)
        else:
            data['prescriptions'] = PrescriptionFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        prescriptions = context['prescriptions']
        
        with transaction.atomic():
            self.object = form.save()
            if prescriptions.is_valid():
                prescriptions.instance = self.object
                prescriptions.save()
            else:
                return self.form_invalid(form)
                
        return super().form_valid(form)