from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Sum
from .forms import MedicineForm, InventoryForm
from .models import Medicine, Inventory
from datetime import timedelta
from django.utils import timezone
def inventory_view(request):
    # Annotate total stock from related Inventory batches
    medicines = Medicine.objects.annotate(
        total_stock=Sum('inventory__current_stock')
    ).order_by('name')
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


def stock_view(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    batches = Inventory.objects.filter(medicine=medicine).order_by('-date_added')
    today = timezone.now().date()
    return render(request, 'stock_view.html', {
        'medicine': medicine,
        'batches': batches,
        'today': today
    })


def add_stock(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == "POST":
        form = InventoryForm(request.POST)
        if form.is_valid():
            # This handles the association automatically
            inventory = form.save(commit=False)
            inventory.medicine = medicine 
            inventory.save()
            return redirect('stock_view', pk=medicine.pk)
    else:
        form = InventoryForm()
    return render(request, 'add_stock.html', {'form': form, 'medicine': medicine})