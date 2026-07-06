from django import forms
from django.forms import inlineformset_factory
from .models import Consultation
from inventory.models import PrescriptionItem, Medicine

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['patient', 'doctor', 'status', 'diagnosis', 'notes']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-select'}),
            'doctor': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'diagnosis': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

class PrescriptionItemForm(forms.ModelForm):
    class Meta:
        model = PrescriptionItem
        fields = ['medicine', 'quantity', 'dosage_instructions', 'duration_days']
        widgets = {
            'medicine': forms.Select(attrs={'class': 'form-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'dosage_instructions': forms.TextInput(attrs={'class': 'form-control'}),
            'duration_days': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }

# This binds the Prescription forms directly to a Consultation instance
PrescriptionFormSet = inlineformset_factory(
    Consultation, 
    PrescriptionItem, 
    form=PrescriptionItemForm,
    extra=1, # Show one empty prescription row by default
    can_delete=True
)