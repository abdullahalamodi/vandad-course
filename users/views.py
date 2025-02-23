from rest_framework import permissions, generics, status, response as rs
from users.models import CustomUser
from utils.custom_response import BaseResponse
from utils.mixins import UserQuerysetMixin
from .serializers import CustomUserRegisterSerializer


class CustomUserRegisterView(generics.CreateAPIView):

    serializer_class = CustomUserRegisterSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class CustomUserListView(
    generics.ListAPIView,
):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserRegisterSerializer
    permission_classes = [
        permissions.IsAdminUser,
    ]

    # def finalize_response(self, request, response, *args, **kwargs):
    #     if isinstance(response, rs.Response):
    #         wrapped_data = {
    #             "status": response.status_code,
    #             "message": "Success" if response.status_code < 400 else "Error",
    #             "data": response.data,
    #         }
    #         response.data = wrapped_data
    #     return super().finalize_response(request, response, *args, **kwargs)
