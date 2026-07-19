from django import forms
from .models import Medicine, Inventory

COMMON_CLASS = 'w-full px-4 py-2.5 bg-white border border-slate-200 rounded-xl text-sm text-slate-800 placeholder-slate-400 shadow-sm focus:outline-none focus:ring-2 focus:ring-cyan-500/40 focus:border-cyan-500 transition'

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'generic_name', 'manufacturer', 'dosage_form', 'strength', 'min_stock_level', 'max_stock_level', 'unit_cost']
        widgets = {
            'name': forms.TextInput(attrs={'class': COMMON_CLASS}),
            'generic_name': forms.TextInput(attrs={'class': COMMON_CLASS}),
            'manufacturer': forms.TextInput(attrs={'class': COMMON_CLASS}),
            'dosage_form': forms.TextInput(attrs={'class': COMMON_CLASS}),
            'strength': forms.TextInput(attrs={'class': COMMON_CLASS}),
            'min_stock_level': forms.NumberInput(attrs={'class': COMMON_CLASS}),
            'max_stock_level': forms.NumberInput(attrs={'class': COMMON_CLASS}),
            'unit_cost': forms.NumberInput(attrs={'class': COMMON_CLASS}),
        }


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['batch_number', 'expiry_date', 'current_stock']
        widgets = {
            'batch_number': forms.TextInput(attrs={'class': COMMON_CLASS}),
            'expiry_date': forms.DateInput(attrs={'class': COMMON_CLASS, 'type': 'date'}),
            'current_stock': forms.NumberInput(attrs={'class': COMMON_CLASS}),
        }
