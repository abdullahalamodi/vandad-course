from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework import status

from utils.custom_response import BaseResponse
from utils.mixins import ResponseWrapperMixin


from .serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(
    ResponseWrapperMixin,
    TokenObtainPairView,
):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        # Get the validated data (tokens + user info)
        data = serializer.validated_data

        # Structure the response
        response = BaseResponse(
            status=status.HTTP_200_OK,
            data={
                "user": {
                    "id": serializer.user.id,
                    "email": serializer.user.email,
                    "date_joined": serializer.user.date_joined,
                },
                "access_token": data["access"],
                "refresh_token": data["refresh"],
            },
        )

        return response
