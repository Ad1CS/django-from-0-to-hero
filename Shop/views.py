from django.http import HttpResponse
from django.shortcuts import render

def mainpage(request):
    return HttpResponse('mainpage')

def about(request):
    return HttpResponse('about')

def product(request):
    return HttpResponse('product')