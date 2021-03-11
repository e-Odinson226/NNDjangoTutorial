from django.shortcuts import render

def homepage(request, *args, **kwargs):
    return render(request, "home.html", {})

def contact(request, *args, **kwargs):
    return render(request, "contact.html", {})

def info(request, *args, **kwargs):
    return render(request, "info.html", {})