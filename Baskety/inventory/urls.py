from django.urls import path
from .views import InventoryDashboardView, StockAdjustmentView

app_name = 'inventory'

from django.views.generic import TemplateView

urlpatterns = [
    path('', InventoryDashboardView.as_view(), name='dashboard'),
    path('adjust/', StockAdjustmentView.as_view(), name='stock_adjustment'),
    path('display/', TemplateView.as_view(template_name='dashboard_display.html'), name='dashboard_display'),
]
