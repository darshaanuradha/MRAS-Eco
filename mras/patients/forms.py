from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['full_name', 'date_of_birth', 'gender', 'phone_number', 'email', 'address', 'medical_notes', 'is_active']
        
        # Matching the CSS from accounts/templates/register.html (same as doctors/forms.py)
        default_input_class = "block w-full px-4 py-2.5 border border-slate-200 rounded-lg bg-slate-50 text-slate-900 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 focus:bg-white transition-colors sm:text-sm"
        
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': default_input_class,
                'placeholder': 'Jane Doe'
            }),
            'date_of_birth': forms.DateInput(attrs={
                'class': default_input_class,
                'type': 'date'
            }),
            'gender': forms.TextInput(attrs={
                'class': default_input_class,
                'placeholder': 'Male, Female, etc.'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': default_input_class,
                'placeholder': '+1 234 567 8900'
            }),
            'email': forms.EmailInput(attrs={
                'class': default_input_class,
                'placeholder': 'patient@example.com'
            }),
            'address': forms.TextInput(attrs={
                'class': default_input_class,
                'placeholder': '123 Main St, City, Country'
            }),
            'medical_notes': forms.Textarea(attrs={
                'class': default_input_class,
                'placeholder': 'Allergies, conditions, etc.',
                'rows': 3
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-emerald-600 focus:ring-emerald-500 border-slate-300 rounded'
            }),
        }
