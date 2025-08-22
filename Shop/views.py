from django.http import HttpResponse
from django.shortcuts import render

def mainpage(request):
    return HttpResponse('mainpage')

def about(request, about_id):
    return HttpResponse(f'about:{about_id}')

def product(request):
    return HttpResponse('product')

def categories(request, cat_id):
    return HttpResponse(f'Category:{cat_id}')
def users(request, users_id):
    return HttpResponse(f'users:{users_id}')
def archive(request, year):
    return HttpResponse(f'archive:{year}')


