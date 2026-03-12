from django.urls import path
from .views import POSView, process_checkout

app_name = 'pos'

urlpatterns = [
    path('', POSView.as_view(), name='index'),
    path('checkout/', process_checkout, name='checkout'),
]
