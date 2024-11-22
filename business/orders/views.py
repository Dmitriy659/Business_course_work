from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch, Sum, F
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView

from .forms import OrderForm
from .models import OrderItem, Order
from .util import check_products
from products.models import Product

import json


@login_required
def user_products(request):
    user_product = Product.objects.filter(user=request.user).values('id', 'title', 'selling_price', 'amount')
    return JsonResponse(list(user_product), safe=False)


class OrderListView(ListView):
    model = Order
    template_name = 'orders/all_orders.html'  # Шаблон для отображения
    context_object_name = 'orders'  # Имя переменной в шаблоне
    paginate_by = 10

    def get_queryset(self):
        order_items = OrderItem.objects.select_related('product')
        orders = (Order.objects.prefetch_related(Prefetch('order', queryset=order_items))
                  .filter(user=self.request.user).order_by('-created'))

        for order in orders:
            order.total_price = sum(
                item.price * item.quantity for item in order.order.all()
            )
        return orders

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        revenue = \
        (OrderItem.objects.filter(order__user=self.request.user).annotate(total_price=F('price') * F('quantity'))
         .aggregate(total_revenue=Sum('total_price')))['total_revenue'] or 0
        context['revenue'] = revenue
        return context


class OrderDeleteView(LoginRequiredMixin, View):
    model = Order
    template_name = 'orders/delete_order.html'
    success_url = reverse_lazy('orders:all_orders')

    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk, user=self.request.user)
        return render(request, 'orders/delete_order.html', {'order': order})

    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk, user=self.request.user)
        return_products = request.POST.get('return_products') == 'on'
        if return_products:
            for item in order.order.all():
                product = item.product
                product.amount += item.quantity
                product.save()
        order.delete()
        return redirect('orders:all_orders')


class CreateOrderView(LoginRequiredMixin, View):
    def get(self, request):
        form = OrderForm()
        return render(request, 'orders/create_order.html', {'form': form})

    def post(self, request):
        errors_log = set()

        data = json.loads(request.body)
        form_data = request.POST.copy()
        form_data['buyer'] = data.get('buyer')
        form = OrderForm(form_data)
        if check_products(data, request.user.id, errors_log) and form.is_valid():
            order = form.save(commit=False)
            order.user = request.user

            products_to_save = dict()
            for product in data['products']:
                product_id = product.get('product_id')
                price = float(product.get('price'))
                quantity = float(product.get('quantity'))

                product_obj = Product.objects.get(id=product_id, user=request.user)
                product_obj.amount -= Decimal(quantity)
                if product_id in products_to_save:
                    products_to_save[product_id] += quantity
                else:
                    products_to_save[product_id] = {'product': product_obj, 'quantity': quantity, 'price': price}
            order.save()
            for product in products_to_save:
                data = products_to_save[product]
                data['product'].save()
                OrderItem.objects.create(order=order, product=data['product'], quantity=data['quantity'],
                                         price=data['price'])
            return redirect('homepage:index')
        return JsonResponse({'error': ' '.join(list(errors_log))}, status=400)
