from django.urls import path
from .views import (    homepage,
                        contact,
                        info)

app_name = "blog"
urlpatterns =[
    path('', homepage, name="homepage"),
    path('contact/', contact, name="contact"),
    path('about/', info, name="info"),
]