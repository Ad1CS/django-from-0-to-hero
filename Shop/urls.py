from django.urls import path

from Shop.views import mainpage, about, product, categories

urlpatterns = [
    path('',product),
    path('Categories/<slug:cat_id>', categories)
]