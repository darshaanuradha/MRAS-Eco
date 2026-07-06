from datetime import date, timedelta
from django.db.models import Sum, F
from django.db.models.functions import Coalesce
from .models import Medicine, Inventory

def inventory_notifications(request):
    # Don't run queries if the user isn't logged in
    if not request.user.is_authenticated:
        return {}

    today = date.today()
    thirty_days_from_now = today + timedelta(days=30)

    # 1. Expired Medicines
    expired_batches = Inventory.objects.filter(
        current_stock__gt=0,
        expiry_date__lt=today
    ).select_related('medicine')

    # 2. Expiring Soon (Next 30 Days)
    expiring_soon_batches = Inventory.objects.filter(
        current_stock__gt=0,
        expiry_date__range=(today, thirty_days_from_now)
    ).select_related('medicine')

    # 3. Low Stock (Total stock <= min_stock_level)
    # We use Coalesce to handle medicines that have 0 batches in the inventory table
    low_stock_medicines = Medicine.objects.annotate(
        total_stock=Coalesce(Sum('inventory__current_stock'), 0)
    ).filter(
        total_stock__lte=F('min_stock_level')
    )

    # Calculate total count for the red notification badge
    notification_count = expired_batches.count() + expiring_soon_batches.count() + low_stock_medicines.count()

    return {
        'notif_count': notification_count,
        'expired_alerts': expired_batches,
        'expiring_alerts': expiring_soon_batches,
        'low_stock_alerts': low_stock_medicines,
    }