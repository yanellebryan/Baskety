from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Sum, Count, F
from pos.models import Transaction, TransactionItem
from products.models import Product

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

@login_required
def dashboard(request):
    # Get today's date
    today = timezone.now().date()
    
    # Today's sales and transaction count (only completed transactions)
    today_transactions = Transaction.objects.filter(
        created_at__date=today,
        status='completed'
    )
    today_sales = today_transactions.aggregate(
        total=Sum('total_amount')
    )['total'] or 0
    transaction_count = today_transactions.count()
    
    # Low stock alerts - products below reorder level
    low_stock_count = Product.objects.filter(
        is_active=True,
        current_stock__lte=F('reorder_level')
    ).count()
    
    # Top product - most sold product (by quantity) from completed transactions
    top_product_data = TransactionItem.objects.filter(
        transaction__status='completed'
    ).values('product_name').annotate(
        total_sold=Sum('quantity')
    ).order_by('-total_sold').first()
    
    top_product = top_product_data['product_name'] if top_product_data else 'N/A'
    
    context = {
        'today_sales': today_sales,
        'transaction_count': transaction_count,
        'low_stock_count': low_stock_count,
        'top_product': top_product,
    }
    
    return render(request, 'dashboard.html', context)
