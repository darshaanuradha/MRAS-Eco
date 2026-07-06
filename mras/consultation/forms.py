from django import forms
from django.forms import inlineformset_factory
from .models import Consultation
from inventory.models import PrescriptionItem, Medicine

# Base Tailwind classes for inputs to keep the code clean
TW_INPUT = "mt-1 block w-full rounded-md border border-gray-300 bg-white py-2 px-3 text-sm shadow-sm focus:border-emerald-500 focus:outline-none focus:ring-1 focus:ring-emerald-500"

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

# Binds the Prescription forms directly to a Consultation instance
PrescriptionFormSet = inlineformset_factory(
    Consultation, 
    PrescriptionItem, 
    form=PrescriptionItemForm,
    extra=1, 
    can_delete=True
)