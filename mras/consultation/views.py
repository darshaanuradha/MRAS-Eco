from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib import messages
from .models import Consultation
from .forms import ConsultationForm, PrescriptionFormSet
from inventory.models import Inventory, PrescriptionAllocation

# --- FEFO Stock Deduction Logic ---
def dispense_stock(consultation):
    """
    Deducts stock automatically based on Earliest Expiry First.
    Only processes items that haven't been deducted yet.
    """
    for item in consultation.prescriptionitem_set.all():
        # IMPORTANT: This prevents double-deduction. 
        # If the consultation is already 'Completed' and the doctor just edits a text note,
        # it skips medicines that were already deducted.
        if item.allocations.exists():
            continue

        remaining_qty = item.quantity
        
        # Fetch batches with stock, ordered by closest expiry date (FEFO)
        available_batches = Inventory.objects.filter(
            medicine=item.medicine,
            current_stock__gt=0
        ).order_by('expiry_date')

        for batch in available_batches:
            if remaining_qty <= 0:
                break
            
            take_qty = min(remaining_qty, batch.current_stock)
            
            # Deduct from Inventory table
            batch.current_stock -= take_qty
            batch.save()
            
            # Record the transaction linking the prescription to the exact inventory batch
            PrescriptionAllocation.objects.create(
                prescription_item=item,
                inventory_batch=batch,
                quantity=take_qty
            )
            
            remaining_qty -= take_qty

        # If we loop through all batches and still need more, block the save.
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
                self.object = form.save()
                if prescriptions.is_valid():
                    prescriptions.instance = self.object
                    prescriptions.save()
                    
                    # TRIGGER: Only deduct stock if creating a brand new 'Completed' consultation
                    if self.object.status == 'Completed':
                        dispense_stock(self.object)
                else:
                    return self.form_invalid(form)
                    
            messages.success(self.request, "Consultation saved successfully.")
            return super().form_valid(form)
            
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
                self.object = form.save()
                if prescriptions.is_valid():
                    prescriptions.instance = self.object
                    prescriptions.save()
                    
                    # TRIGGER: If user changes status from 'Pending' to 'Completed', this runs.
                    if self.object.status == 'Completed':
                        dispense_stock(self.object)
                else:
                    return self.form_invalid(form)
                    
            messages.success(self.request, "Consultation updated successfully.")
            return super().form_valid(form)
            
        except ValueError as e:
            # If there isn't enough stock, it shows an error message and prevents saving
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