from django.urls import path

from Shop.views import mainpage, about, product

urlpatterns = [
    path('',product)
]