from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from patients.models import Patient
from consultation.models import Consultation
from inventory.models import Medicine
from doctors.models import Doctor


from django.db.models import Sum, F

@login_required(login_url='login')
def home(request):
    today = timezone.now().date()
    
    # Calculate real-time metrics
    patients_total = Patient.objects.count()
    pending_consultations = Consultation.objects.filter(status='Pending').count()
    active_doctors = Doctor.objects.filter(is_active=True).count()
    
    # Calculate low stock count
    low_stock_medicines = Medicine.objects.annotate(
        total_stock=Sum('inventory__current_stock')
    ).filter(total_stock__lt=F('min_stock_level'))
    
    low_stock_count = low_stock_medicines.count()

    # Fetch the actual low stock medicine objects
    low_stock_medicines = Medicine.objects.annotate(
        total_stock=Sum('inventory__current_stock')
    ).filter(total_stock__lt=F('min_stock_level'))

    low_stock_count = low_stock_medicines.count()
    # Get 5 most recent pending consultations
    recent_consultations = Consultation.objects.filter(
        status='Pending'
    ).select_related('patient', 'doctor').order_by('-consultation_date')[:5]

    context = {
        'patients_total': patients_total,
        'pending_consultations': pending_consultations,
        'active_doctors': active_doctors,
        'low_stock_count': low_stock_count,
        'recent_consultations': recent_consultations,
        'low_stock_medicines': low_stock_medicines,
    }
    return render(request, 'home.html', context)

# REGISTER
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # validation
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')

        # create user (IMPORTANT: username = email)
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        user.save()
        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'register.html')


# LOGIN
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # authenticate using username=email
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password")
            return redirect('login')

    return render(request, 'login.html')

# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')