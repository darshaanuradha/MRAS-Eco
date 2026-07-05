from django.db import models
class Medicine(models.Model):
    name = models.CharField(max_length=100, unique=True)
    generic_name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    dosage_form = models.CharField(max_length=50, blank=True, null=True)
    strength = models.CharField(max_length=50, blank=True, null=True)
    min_stock_level = models.IntegerField(default=20)
    max_stock_level = models.IntegerField(default=500)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['generic_name']),
        ]

    def __str__(self):
        return self.name    
    


class Inventory(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    batch_number = models.CharField(max_length=50, unique=True)
    expiry_date = models.DateField()
    current_stock = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['batch_number']),
            models.Index(fields=['expiry_date']),
        ]

    def __str__(self):
        return f"{self.medicine.name} - Batch: {self.batch_number}"