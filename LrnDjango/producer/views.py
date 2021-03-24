from django.shortcuts import render, redirect
from .models import Profile
from .forms import (    ProducerRegForm,
                        ProducerUpdForm,
                        ProfileUpdForm,)
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register_view(request):
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

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = ProducerUpdForm(request.POST, instance=request.user)
        p_form = ProfileUpdForm(    request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            
            messages.success(request, f'Your acount has been Updated.') 
            return redirect('profile')
    else:
        u_form = ProducerUpdForm(instance=request.user)
        p_form = ProfileUpdForm(instance=request.user.profile)
        
    context = {
        "u_form" : u_form,
        "p_form" : p_form
    }
    return render(request, 'producer/profile.html', context)

    
