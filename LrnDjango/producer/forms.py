from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class ProducerRegForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class ProducerUpdForm(forms.ModelForm):
    email  = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['logo']
