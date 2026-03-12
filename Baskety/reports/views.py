from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.decorators import RoleRequiredMixin
from django.db.models import Sum, Count, F, FloatField
from django.db.models.functions import TruncDay
from django.utils import timezone
from datetime import timedelta
from pos.models import Transaction, TransactionItem

class ReportsDashboardView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    allowed_roles = ['admin', 'manager']
    template_name = 'reports/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        today = now.date()
        week_start = now - timedelta(days=7)

        # Today's Sales
        today_txns = Transaction.objects.filter(created_at__date=today, status='completed')
        context['today_sales'] = today_txns.aggregate(total=Sum('total_amount'))['total'] or 0
        context['today_orders'] = today_txns.count()
        
        # Best Selling Products (Top 5)
        top_products = TransactionItem.objects.filter(transaction__status='completed')\
            .values('product_name')\
            .annotate(total_qty=Sum('quantity'), total_rev=Sum('subtotal'))\
            .order_by('-total_qty')[:5]
        context['top_products'] = top_products

        # Weekly Sales Trend (Last 7 days)
        # SQLite datetime extraction might be tricky, using TruncDay for Django > 2.0
        daily_sales = Transaction.objects.filter(created_at__gte=week_start, status='completed')\
            .annotate(day=TruncDay('created_at'))\
            .values('day')\
            .annotate(total=Sum('total_amount'), count=Count('id'))\
            .order_by('day')
            
        labels = []
        data = []
        for x in daily_sales:
            labels.append(x['day'].strftime('%a %d'))
            data.append(float(x['total']))
        
        context['chart_labels'] = labels
        context['chart_data'] = data
        
        return context
