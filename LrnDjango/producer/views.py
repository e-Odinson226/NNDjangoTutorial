from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProducerRegForm

def producer_reg(request):
    if request.method == "POST":
        form = ProducerRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            return redirect('login')
    else:
        form = ProducerRegForm()
    context ={
        "form" : form
    }
    return render(request, "producer/register.html", context)
#--------------------------------------------------------------------
