from django.urls import path

from Shop.views import mainpage, about, product, categories

urlpatterns = [
    path('',product),
    path('Categories/<int:cat_id>', categories)
]