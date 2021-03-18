from django.forms import ModelForm
from .models import Producer

class ProducerForm(ModelForm):
    class Meta:
        model = Producer
        fields =[
            'name',
            'address',
            'desc',
            'reg_id',
            'logo'
        ]