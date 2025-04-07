from django.urls import path
from userauths import views

app_name = "userauths"

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("login/", views.login, name="login"),
    
]
