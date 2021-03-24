from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (    register_view,
                        profile )

app_name = "producer"
urlpatterns =[
    path('register/',   register_view,          name="register"),

    path('profile/',    profile,                name="profile"),

    path('log-in/',     LoginView.as_view(
        template_name='producer/login.html'),   name="login"),

    path('log-out/',    LogoutView.as_view(
        template_name='producer/logout.html'),  name="logout"),

]