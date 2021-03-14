from django.shortcuts import render
from .models import Product

def product_single_view(request, id):
    obj = Product.objects.get(id=id)
    context ={
        "title" : obj.title,
        "description" : obj.description,
        "price" : obj.price,
    }
    return render(request, "product/detail.html", context)
