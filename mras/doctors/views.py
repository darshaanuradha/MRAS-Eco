from django.shortcuts import render

def doctors_view(request):
    return render(request, 'doctors.html')
