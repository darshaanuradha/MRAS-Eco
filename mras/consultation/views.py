from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib import messages
from .models import Consultation
from .forms import ConsultationForm, PrescriptionFormSet
from inventory.models import Inventory, PrescriptionAllocation

# --- FEFO Stock Deduction Logic ---
def dispense_stock(consultation):
    for item in consultation.prescriptionitem_set.all():
        if item.allocations.exists():
            continue

        remaining_qty = item.quantity
        available_batches = Inventory.objects.filter(
            medicine=item.medicine,
            current_stock__gt=0
        ).order_by('expiry_date')

        for batch in available_batches:
            if remaining_qty <= 0:
                break
            
            take_qty = min(remaining_qty, batch.current_stock)
            
            batch.current_stock -= take_qty
            batch.save()
            
            PrescriptionAllocation.objects.create(
                prescription_item=item,
                inventory_batch=batch,
                quantity=take_qty
            )
            
            remaining_qty -= take_qty

        if remaining_qty > 0:
            raise ValueError(f"Insufficient stock for {item.medicine.name}. Short by {remaining_qty} units.")


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
        
        try:
            with transaction.atomic():
                # Check if BOTH the main form and the prescriptions have enough stock
                if form.is_valid() and prescriptions.is_valid():
                    self.object = form.save()
                    prescriptions.instance = self.object
                    prescriptions.save()
                    
                    if self.object.status == 'Completed':
                        dispense_stock(self.object)
                        
                    messages.success(self.request, "Consultation saved successfully.")
                    return super().form_valid(form)
                else:
                    # If stock check fails, extract the formset errors and display them as messages
                    for error_dict in prescriptions.errors:
                        for field, errors in error_dict.items():
                            for error in errors:
                                messages.error(self.request, error)
                    return self.form_invalid(form)
                    
        except ValueError as e:
            messages.error(self.request, str(e))
            return self.render_to_response(self.get_context_data(form=form))


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
        
        try:
            with transaction.atomic():
                if form.is_valid() and prescriptions.is_valid():
                    self.object = form.save()
                    prescriptions.instance = self.object
                    prescriptions.save()
                    
                    if self.object.status == 'Completed':
                        dispense_stock(self.object)
                        
                    messages.success(self.request, "Consultation updated successfully.")
                    return super().form_valid(form)
                else:
                    for error_dict in prescriptions.errors:
                        for field, errors in error_dict.items():
                            for error in errors:
                                messages.error(self.request, error)
                    return self.form_invalid(form)
                    
        except ValueError as e:
            messages.error(self.request, str(e))
            return self.render_to_response(self.get_context_data(form=form))


class ConsultationPrintView(DetailView):
    model = Consultation
    template_name = 'consultation_print.html'
    context_object_name = 'consultation'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prescription_items'] = self.object.prescriptionitem_set.prefetch_related('allocations__inventory_batch').all()
        return context