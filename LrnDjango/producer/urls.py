from django.urls import path
from .views import ( producer_reg )

app_name = "producer"
urlpatterns =[
    path('register/', producer_reg, name="producerDetail")
]