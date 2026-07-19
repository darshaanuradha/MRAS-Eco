from django import forms
from django.forms import inlineformset_factory
from django.db.models import Sum
from .models import Consultation
from inventory.models import PrescriptionItem, Medicine, Inventory

# Base Tailwind classes for inputs
TW_INPUT = "mt-1 block w-full rounded-xl border border-slate-200 bg-white py-2.5 px-4 text-sm shadow-sm focus:border-cyan-500 focus:outline-none focus:ring-2 focus:ring-cyan-500/40 transition"

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['patient', 'doctor', 'status', 'diagnosis', 'notes']
        widgets = {
            'patient': forms.Select(attrs={'class': TW_INPUT}),
            'doctor': forms.Select(attrs={'class': TW_INPUT}),
            'status': forms.Select(attrs={'class': TW_INPUT}),
            'diagnosis': forms.Textarea(attrs={'class': TW_INPUT, 'rows': 3, 'placeholder': 'Enter detailed medical diagnosis...'}),
            'notes': forms.Textarea(attrs={'class': TW_INPUT, 'rows': 2, 'placeholder': 'Any additional observations (optional)...'}),
        }

class PrescriptionItemForm(forms.ModelForm):
    class Meta:
        model = PrescriptionItem
        fields = ['medicine', 'quantity', 'dosage_instructions', 'duration_days']
        widgets = {
            'medicine': forms.Select(attrs={'class': TW_INPUT}),
            'quantity': forms.NumberInput(attrs={'class': TW_INPUT, 'min': 1, 'placeholder': 'Qty'}),
            'dosage_instructions': forms.TextInput(attrs={'class': TW_INPUT, 'placeholder': 'e.g., 1 tablet after meals'}),
            'duration_days': forms.NumberInput(attrs={'class': TW_INPUT, 'min': 1, 'placeholder': 'Days'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        medicine = cleaned_data.get('medicine')
        quantity = cleaned_data.get('quantity')
        delete_flag = cleaned_data.get('DELETE', False)

        # If the user is removing this row, we don't need to check stock
        if delete_flag:
            return cleaned_data

        # Check if this item was ALREADY dispensed (so we don't block saving if they edit an old completed consultation)
        is_dispensed = self.instance.pk and self.instance.allocations.exists()

        if medicine and quantity and not is_dispensed:
            # Calculate total stock available across all batches for this medicine
            total_stock = Inventory.objects.filter(
                medicine=medicine,
                current_stock__gt=0
            ).aggregate(total=Sum('current_stock'))['total'] or 0

            # Block the form if they prescribe more than the inventory holds
            if quantity > total_stock:
                error_msg = f"Cannot prescribe {quantity}x {medicine.name}. Only {total_stock} units available in inventory."
                
                # Attach error to the quantity field
                self.add_error('quantity', f"Only {total_stock} available.")
                # Attach a global error so it can be passed to the Django messages framework
                raise forms.ValidationError(error_msg)

        return cleaned_data

# Binds the Prescription forms directly to a Consultation instance
PrescriptionFormSet = inlineformset_factory(
    Consultation, 
    PrescriptionItem, 
    form=PrescriptionItemForm,
    extra=1, 
    can_delete=True
)