from django.shortcuts import render, get_object_or_404
from .models import Patient

def patient_list(request):
    query = request.GET.get('q', '')
    if query:
        patients = Patient.objects.filter(name__icontains=query)
    else:
        patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients, 'query': query})

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patients/patient_detail.html', {'patient': patient})