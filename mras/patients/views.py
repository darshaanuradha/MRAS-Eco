from django.shortcuts import render

def patients_view(request):
    return render(request, 'patients.html')