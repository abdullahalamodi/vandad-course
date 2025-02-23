from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from authtokens.views import CustomTokenObtainPairView


app_name: str = "authtokens"

urlpatterns = [
    path("", CustomTokenObtainPairView.as_view(), name="token_optain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token-refresh"),
]
