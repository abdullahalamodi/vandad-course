from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import CustomUser


class CustomUserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=CustomUser.objects.all(),
                lookup="iexact",
            )
        ],
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[
            validate_password,
        ],
        style={
            "input_type": "password",
        },
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={
            "input_type": "password",
        },
    )

    create_at = serializers.CharField(source="date_joined", read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "password",
            "password2",
            "create_at",
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Passwords must match."},
            )
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        return CustomUser.objects.create_user(  # type:ignore
            **validated_data,
        )
