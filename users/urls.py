from django.urls import path

from .views import CustomUserListView, CustomUserRegisterView

app_name = "users"

urlpatterns = [
    path("register/", CustomUserRegisterView.as_view(), name="register"),
    path("", CustomUserListView.as_view(), name="users-list"),
]
