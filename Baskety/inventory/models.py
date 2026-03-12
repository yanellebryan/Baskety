from django.db import models
from django.conf import settings
from products.models import Product

class StockMovement(models.Model):
    MOVEMENT_TYPES = (
        ('restock', 'Restock'),
        ('sale', 'Sale'),
        ('adjustment', 'Adjustment (Loss/Damage)'),
        ('return', 'Return'),
    )
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='movements')
    movement_type = models.CharField(max_length=20, choices=MOVEMENT_TYPES)
    quantity = models.IntegerField(help_text="Positive for addition, negative for deduction (except Sale which is auto-negated in logic)")
    reason = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_movement_type_display()} - {self.product.name} ({self.quantity})"
