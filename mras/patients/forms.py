from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'contact', 'address', 'medical_history']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'age': forms.NumberInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'gender': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'contact': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'address': forms.Textarea(attrs={'class': 'w-full border rounded px-3 py-2', 'rows': 3}),
            'medical_history': forms.Textarea(attrs={'class': 'w-full border rounded px-3 py-2', 'rows': 4}),
        }
