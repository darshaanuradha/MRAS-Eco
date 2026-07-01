from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Doctor
from .forms import DoctorForm

@login_required(login_url='login')
def doctor_list(request):
    doctors = Doctor.objects.all().order_by('-created_at')
    # Assuming templates will be placed in a 'doctors' subdirectory
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})

@login_required(login_url='login')
def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor created successfully.')
            return redirect('doctors:list')
    else:
        form = DoctorForm()
    return render(request, 'doctors/doctor_form.html', {'form': form, 'title': 'Add New Doctor'})

@login_required(login_url='login')
def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor updated successfully.')
            return redirect('doctors:list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctors/doctor_form.html', {'form': form, 'title': 'Edit Doctor', 'doctor': doctor})

@login_required(login_url='login')
def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        messages.success(request, 'Doctor deleted successfully.')
        return redirect('doctors:list')
    return render(request, 'doctors/doctor_confirm_delete.html', {'doctor': doctor})
