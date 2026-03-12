from django.db import models
from django.utils.text import slugify

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(upload_to='categories/', blank=True, null=True)
    icon_name = models.CharField(max_length=50, default='box', help_text="Lucide icon name (e.g. 'milk', 'carrot')")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    UNIT_CHOICES = (
        ('pcs', 'Pieces'),
        ('pack', 'Pack'),
        ('box', 'Box'),
        ('kg', 'Kilograms'),
        ('g', 'Grams'),
        ('l', 'Liters'),
        ('ml', 'Milliliters'),
        ('can', 'Can'),
        ('bottle', 'Bottle'),
        ('sachet', 'Sachet'),
        ('tray', 'Tray'),
        ('dozen', 'Dozen'),
        ('bundle', 'Bundle'),
    )
    
    sku = models.CharField(max_length=50, unique=True, help_text="Stock Keeping Unit / Barcode")
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    
    # Pricing
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_applicable = models.BooleanField(default=True)
    
    # Stock
    current_stock = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=10, help_text="Low stock threshold")
    reorder_quantity = models.IntegerField(default=50, help_text="Suggested restock amount")
    
    unit_of_measure = models.CharField(max_length=10, choices=UNIT_CHOICES, default='pcs')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.sku})"

    @property
    def stock_status(self):
        if self.current_stock <= 0:
            return 'Out of Stock'
        elif self.current_stock <= self.reorder_level:
            return 'Critical'
        elif self.current_stock <= (self.reorder_level + 50):
            return 'Low Stock'
        return 'In Stock'
