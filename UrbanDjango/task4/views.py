from django.shortcuts import render

# Главная страница
def main_page(request):
    menu_items = [
        {'title': 'Главная', 'url_name': 'main_page'},
        {'title': 'Магазин', 'url_name': 'shop_page'},
        {'title': 'Корзина', 'url_name': 'cart_page'}
    ]
    return render(request, 'forth_task/main_page.html', {'menu_items': menu_items})

# Первая доп. страница: Магазин
def shop_page(request):
    items = {
        'item1': 'Товар 1',
        'item2': 'Товар 2',
        'item3': 'Товар 3'
    }
    return render(request, 'forth_task/shop_page.html', {'items': items})

# Вторая доп. страница: Корзина
def cart_page(request):
    context = {
        'games': ['Atomic Heart', 'Cyberpunk 2077']  # Список с играми
    }
    return render(request, 'forth_task/cart_page.html', context)
