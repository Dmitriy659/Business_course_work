from django.db.models import Sum, F
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .models import Product
from .forms import ProductForm
from categories.models import Category


class ProductListView(ListView):
    model = Product
    form_class = ProductForm
    template_name = 'products/all_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        context['category'] = Category.objects.get(pk=category_id)
        context['products'] = Product.objects.filter(user=self.request.user,
                                                     category=category_id)
        return context


class CreateProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/create_product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = Category.objects.get(pk=category_id,
                                        user=self.request.user)
        context['category'] = category
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user  # Привязываем товар к текущему пользователю
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id, user=self.request.user)
        form.instance.category = category
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('products:all_products', kwargs={'category_id': self.kwargs.get('category_id')})


class UpdateProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/update_product.html'

    def get_object(self, queryset=None):
        category_id = self.kwargs.get('category_id')
        return get_object_or_404(
            Product,
            pk=self.kwargs.get('pk'),
            user=self.request.user,
            category_id=category_id
        )

    def get_success_url(self):
        return reverse_lazy('products:all_products', kwargs={'category_id': self.kwargs.get('category_id')})


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'products/delete_product.html'

    def get_object(self, queryset=None):
        category_id = self.kwargs.get('category_id')
        return get_object_or_404(
            Product,
            pk=self.kwargs.get('pk'),
            user=self.request.user,
            category_id=category_id
        )

    def get_success_url(self):
        return reverse_lazy('products:all_products', kwargs={'category_id': self.kwargs.get('category_id')})


class HeapProductListView(ListView):
    model = Product
    form_class = ProductForm
    template_name = 'products/heap_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        sort_type = self.request.GET.get('sort', 'title')
        if sort_type not in ['title', '-title', 'selling_price', '-selling_price',
                             'total_sales', '-total_sales', 'total_revenue', '-total_revenue']:
            sort_type = 'title'

        products = Product.objects.filter(user=self.request.user)

        products = products.annotate(
            total_sales=Sum('product__quantity'),
            total_revenue=Sum(F('product__quantity') * F('product__price'))
        )

        return products.order_by(sort_type)


