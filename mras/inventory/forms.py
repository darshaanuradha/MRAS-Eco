from django import forms
from .models import Medicine

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'generic_name', 'manufacturer', 'dosage_form', 'strength', 'min_stock_level', 'max_stock_level', 'unit_cost']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'generic_name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'manufacturer': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'dosage_form': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'strength': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'min_stock_level': forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'max_stock_level': forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'unit_cost': forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
        }