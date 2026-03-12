from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import StockMovement

@receiver(post_save, sender=StockMovement)
def update_product_stock(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        # Logic: If movement is 'restock' or 'return', add.
        # If 'sale' or 'adjustment' (usually negative), add directly if input is negative, 
        # but let's standardize: 
        # If the user enters +5 for Restock, it adds.
        # If user enters 5 for Sale, it subtracts? Or system records -5?
        
        # Let's assume the 'quantity' field in StockMovement carries the sign.
        # EXCEPT for 'Sale' where usually we just say "sold 5".
        
        # But for simplicity, let's trust the sign in the quantity field for now, 
        # OR handle purely by type.
        
        # Refined Logic based on typical usage:
        # Restock: +qty
        # Return: +qty
        # Sale: -qty
        # Adjustment: +/- qty (user defines sign)
        
        qty = instance.quantity
        if instance.movement_type == 'sale':
            qty = -abs(qty) # Ensure it's negative
        elif instance.movement_type in ['restock', 'return']:
            qty = abs(qty) # Ensure it's positive
        # Adjustment takes the sign as given
        
        product.current_stock += qty
        product.save()
