from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=20)
    address = models.TextField()
    medical_history = models.TextField(blank=True, null=True)

    @property
    def full_name(self):
        return self.name

    def __str__(self):
        return self.name
