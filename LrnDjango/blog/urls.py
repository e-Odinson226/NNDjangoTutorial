from django.urls import path
from .views import (    articles,
                        contact,
                        info)

app_name = "blog"
urlpatterns =[
    path('articles/', articles, name="articles"),
    path('contact/', contact, name="contact"),
    path('about/', info, name="info"),
]