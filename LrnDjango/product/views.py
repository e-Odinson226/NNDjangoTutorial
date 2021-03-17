from django.shortcuts import render, get_object_or_404, redirect
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
    #obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    context ={
        "title" : obj.title,
        "description" : obj.description,
        "price" : obj.price,
    }
    return render(request, "product/detail.html", context)

def product_delete_view(request, id):
    #obj = Product.objects.get(id=id)        
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("../../")
    context ={
        "object" : obj
    }
    return render(request, "product/delete.html", context)