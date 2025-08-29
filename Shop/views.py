from django.http import HttpResponse
from django.shortcuts import render

def mainpage(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def product(request, products_id):
    return render(request, 'products.html')

def categories(request, cat_id):
    return HttpResponse(f'Category:{cat_id}')
def users(request, users_id):
    return HttpResponse(f'users:{users_id}')
def archive(request, year):
    return HttpResponse(f'archive:{year}')



