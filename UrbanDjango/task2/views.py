from django.shortcuts import render
import os
from django.conf import settings

def class_based_view(request):
    print("Ищем шаблон по пути:",
          os.path.join(settings.BASE_DIR, 'task2/templates/second_task/class_view_template.html'))  # Вывод пути
    return render(request, 'second_task/class_view_template.html')

def function_based_view(request):
    return render(request, 'second_task/function_view_template.html')



