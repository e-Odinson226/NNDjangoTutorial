from django.shortcuts import render
from .models import Product
from .forms import ProductForm

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context ={
        "form" : form
    }
    return render(request, "product/create.html", context)

def products_view(request):
    obj_list = Product.objects.all()
    context ={
        "products" : obj_list
    }
    return render(request, "product/products.html", context)

def product_single_view(request, id):
    obj = Product.objects.get(id=id)
    context ={
        "title" : obj.title,
        "description" : obj.description,
        "price" : obj.price,
    }
    return render(request, "product/detail.html", context)
