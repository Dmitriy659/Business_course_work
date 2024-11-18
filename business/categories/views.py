from django.shortcuts import render

from .forms import CategoryForm


def all_categories(request):
    """
    Начальная страница с категориями, тут можно посмотреть их все, а также есть кнопка создания
    """
    return render(request, 'categories/categories.html')


def create_category(request):
    """
    Страница с формой для создания категории
    :param request:
    :return:
    """
    form = CategoryForm(request.POST or None)
    context = {'form': form}
    return render(request, 'categories/create_category.html', context=context)
