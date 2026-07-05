from django.shortcuts import get_object_or_404, render, redirect

from .forms import MedicineForm
from .models import Medicine

# Create your views here.

def inventory_view(request):
    medicines = Medicine.objects.all().order_by('name')
    return render(request, 'inventory.html', {'medicines': medicines})

def add_medicine(request):
    if request.method == "POST":
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form = MedicineForm()
    return render(request, 'add_medicine.html', {'form': form})

def edit_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == "POST":
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form = MedicineForm(instance=medicine)
    return render(request, 'edit_medicine.html', {'form': form, 'medicine': medicine})

def delete_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == "POST":
        medicine.delete()
        return redirect('inventory')
    return render(request, 'confirm_delete.html', {'medicine': medicine})