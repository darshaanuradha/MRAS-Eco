from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['full_name', 'specialization', 'phone_number', 'email', 'is_active']
        
        # Matching the CSS from accounts/templates/register.html
        # Note: 'pl-10' was changed to 'px-4' assuming you might not render the absolute positioned SVG icons inside the inputs for this form.
        default_input_class = "block w-full px-4 py-2.5 border border-slate-200 rounded-lg bg-slate-50 text-slate-900 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 focus:bg-white transition-colors sm:text-sm"
        
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
                'class': 'h-4 w-4 text-emerald-600 focus:ring-emerald-500 border-slate-300 rounded'
            }),
        }
