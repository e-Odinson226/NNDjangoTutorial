from django.shortcuts import render

def articles(request, *args, **kwargs):
    
    return render(request, "articles_all.html", {})

def contact(request, *args, **kwargs):
    return render(request, "contact.html", {})

def info(request, *args, **kwargs):
    return render(request, "info.html", {})