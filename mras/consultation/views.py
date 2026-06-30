from django.shortcuts import render

def consultation_view(request):
    return render(request, 'consultation.html')