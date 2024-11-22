from products.models import Product
from decimal import Decimal
from collections import defaultdict


def check_products(data, user_id, errors_log):
    products = Product.objects.filter(user_id=user_id).values('id', 'amount')
    products_dict = {}
    products_to_new_check = defaultdict(Decimal)
    print(data['products'])
    for product in products:
        products_dict[str(product['id'])] = product['amount']
    if not data['products']:
        errors_log.add('Заказ пуст')
        return False
    for product in data['products']:
        try:
            if product['product_id'] in products_dict:
                try:
                    round(float(product['price']))
                except Exception as e:
                    errors_log.add('Проверьте корректность цены')
                    return False
                quantity = Decimal(float(product['quantity']))
                if quantity > products_dict[product['product_id']]:
                    errors_log.add('Кол-во товара превышает остаток')
                    return False
                products_to_new_check[product['product_id']] += quantity
            else:
                errors_log.addd('Одного из товаров у вас нет')
                return False
        except Exception as e:
            return False

    for product in products_to_new_check:
        if products_to_new_check[product] > products_dict[product]:
            errors_log.add('Кол-во товара превышает остаток')
            return False
    return True
