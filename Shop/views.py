from django.http import HttpResponse
from django.shortcuts import render
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def mainpage(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'float': 28.56,
        'lst': [1, 2, 'abc', True],
        'set': {1, 1, 2, 3, 2, 5},
        'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
        'obj': MyClass(10, 20),
    }
    return render(request, 'index.html', data)

def about(request):
    return render(request, 'about.html',{'menu':menu})

def product(request, products_id):
    return render(request, 'products.html')

def categories(request, cat_id):
    return HttpResponse(f'Category:{cat_id}')
def users(request, users_id):
    return HttpResponse(f'users:{users_id}')
def archive(request, year):
    return HttpResponse(f'archive:{year}')



