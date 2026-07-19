from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['full_name', 'specialization', 'phone_number', 'email', 'is_active']
        
        default_input_class = "w-full px-4 py-2.5 bg-white border border-slate-200 rounded-xl text-sm text-slate-800 placeholder-slate-400 shadow-sm focus:outline-none focus:ring-2 focus:ring-cyan-500/40 focus:border-cyan-500 transition"
        
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': default_input_class,
                'placeholder': 'Dr. Jane Doe'
            }),
            'specialization': forms.TextInput(attrs={
                'class': default_input_class,
                'placeholder': 'Cardiology, Pediatrics, etc.'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': default_input_class,
                'placeholder': '+1 234 567 8900'
            }),
            'email': forms.EmailInput(attrs={
                'class': default_input_class,
                'placeholder': 'doctor@hospital.com'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 rounded border-slate-300 text-cyan-600 focus:ring-cyan-500'
            }),
        }
