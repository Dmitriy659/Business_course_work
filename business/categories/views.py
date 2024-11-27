from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, F
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .forms import CategoryForm
from .models import Category

REDIRECT_TO = 'categories:all_categories'


class CategoryListView(LoginRequiredMixin, ListView):
    """Страница со всеми категориями"""
    model = Category
    template_name = 'categories/all_categories.html'
    paginate_by = 4

    def get_queryset(self):
        queryset = Category.objects.filter(user=self.request.user).annotate(
            total_sales=Sum('products__product__quantity'),
            total_revenue=Sum(F('products__product__quantity') * F('products__product__price'))
        ).order_by('title')
        return queryset


class UpdateCategoryView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/update_category.html'
    success_url = reverse_lazy(REDIRECT_TO)

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class DeleteCategoryView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'categories/delete_category.html'
    success_url = reverse_lazy(REDIRECT_TO)

    def get_queryset(self):
        categories = Category.objects.filter(user=self.request.user)

        return categories


class CreateCategoryView(LoginRequiredMixin, CreateView):
    """
    Страница создания категории
    """
    model = Category
    form_class = CategoryForm
    template_name = 'categories/create_category.html'
    success_url = reverse_lazy(REDIRECT_TO)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
