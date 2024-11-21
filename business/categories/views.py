from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from .forms import CategoryForm
from .models import Category

REDIRECT_TO = 'categories:all_categories'


class CategoryListView(ListView):
    """
    Страница со всеми категориями
    """
    model = Category
    template_name = 'categories/all_categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(user=self.request.user)
        return context


class UpdateCategoryView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/update_category.html'
    success_url = reverse_lazy(REDIRECT_TO)

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'categories/delete_category.html'
    success_url = reverse_lazy(REDIRECT_TO)

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class CreateCategoryView(CreateView):
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
