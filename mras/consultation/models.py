from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class Consultation(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='consultations')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name='consultations')
    consultation_date = models.DateTimeField(auto_now_add=True)
    diagnosis = models.TextField()
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Completed')

    class Meta:
        db_table = 'consultation_consultation'
        ordering = ['-consultation_date']

    def __str__(self):
        return f"{self.patient.full_name} - {self.consultation_date.strftime('%Y-%m-%d')}"