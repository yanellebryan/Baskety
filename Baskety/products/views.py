from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, Category
from django.db.models import Q

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        category = self.request.GET.get('category')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(sku__icontains=query)
            )
        if category:
            queryset = queryset.filter(category__id=category)
        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['sku', 'name', 'category', 'description', 'image', 'buying_price', 'selling_price', 'tax_applicable', 'current_stock', 'reorder_level', 'unit_of_measure', 'is_active']
    # Start fields fix: model has 'cost_price' not 'buying_price'
    fields = ['sku', 'name', 'category', 'description', 'image', 'cost_price', 'selling_price', 'tax_applicable', 'current_stock', 'reorder_level', 'reorder_quantity', 'unit_of_measure', 'is_active']
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('inventory:dashboard')

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['sku', 'name', 'category', 'description', 'image', 'cost_price', 'selling_price', 'tax_applicable', 'current_stock', 'reorder_level', 'reorder_quantity', 'unit_of_measure', 'is_active']
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('inventory:dashboard')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('inventory:dashboard')
