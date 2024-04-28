from django.db import models
from vendors.models import Vendor
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from datetime import datetime, timedelta
from django.db.models import Avg, Count, F
from django.core.validators import MinValueValidator, MaxValueValidator


from vendors.models import Vendor

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    status = models.CharField(max_length=20)
    quality_rating = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"PO#{self.po_number} - {self.vendor.name}"

# purchase_orders/models.py


class UpdateAcknowledgment (models.Model):
    # fields as defined before
    @receiver(post_save, sender=PurchaseOrder)
    @receiver(post_delete, sender=PurchaseOrder)
    def update_vendor_performance(sender, instance,  **kwargs):
        vendor = instance.vendor

        # Get completed purchase orders for the vendor
        completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')

        if completed_orders.exists():
            # Calculate On-Time Delivery Rate
            on_time_orders = completed_orders.filter(delivery_date__lte=F('acknowledgment_date'))
            on_time_delivery_rate = (on_time_orders.count() / completed_orders.count()) * 100

            # Calculate Quality Rating Average
            quality_rating_avg = completed_orders.aggregate(avg_rating=Avg('quality_rating'))['avg_rating'] or 0

            # Calculate Average Response Time
            response_times = completed_orders.exclude(acknowledgment_date=None).annotate(response_time=F('acknowledgment_date') - F('issue_date'))
            average_response_time = (response_times.aggregate(avg_response=Avg('response_time'))['avg_response'] or 0).total_seconds() / response_times.count() if response_times.exists() else 0

            # Calculate Fulfillment Rate
            fulfilled_orders = completed_orders.exclude(issue_date=None).filter(issue_date__lte=F('delivery_date'))
            fulfillment_rate = (fulfilled_orders.count() / completed_orders.count()) * 100

            # Update vendor performance metrics
            Vendor.objects.filter(pk=vendor.pk).update(
                on_time_delivery_rate=on_time_delivery_rate,
                quality_rating_avg=quality_rating_avg,
                average_response_time=average_response_time,
                fulfillment_rate=fulfillment_rate
            )
        else:
            # If there are no completed orders, reset all metrics to zero
            Vendor.objects.filter(pk=vendor.pk).update(
                on_time_delivery_rate=0,
                quality_rating_avg=0,
                average_response_time=0,
                fulfillment_rate=0
            )