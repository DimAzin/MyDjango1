from django import forms
from django.shortcuts import render
from django.http import HttpResponse

# Псевдо-список пользователей
users = ['user1', 'user2', 'user3']


# Создание формы регистрации
class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Введите пароль')
    repeat_password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Повторите пароль')
    age = forms.IntegerField(label='Введите свой возраст')


def sign_up_by_html(request):
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username in users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = UserRegister()  # Инициализация пустой формы

    info['form'] = form  # Передаем форму в контекст
    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_django(request):
    # Аналогично, добавьте логику для этого представления
    return HttpResponse("Это представление для регистрации через Django")
