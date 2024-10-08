from django.shortcuts import render

# Главная страница
def main_page(request):
    return render(request, 'third_task/main_page.html')

# Первая доп. страница: Магазин
def shop_page(request):
    items = {
        'item1': 'Товар 1',
        'item2': 'Товар 2',
        'item3': 'Товар 3'
    }
    return render(request, 'third_task/shop_page.html', {'items': items})

# Вторая доп. страница: Корзина
def cart_page(request):
    return render(request, 'third_task/cart_page.html')

