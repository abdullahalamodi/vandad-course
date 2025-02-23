from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email adress")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(
            email=email,
            password=password,
            **extra_fields,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user
