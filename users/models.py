from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, User
from users.managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    class RegistrationSource(models.TextChoices):
        LOCAL = 'local', 'Local'
        GOOGLE = 'google', 'Google'
        FACEBOOK = 'facebook', 'Facebook'

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150, blank=True, default='')
    last_name = models.CharField(max_length=150, blank=True, default='')
    phone_number = models.CharField(max_length=20, blank=True, default='')
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    birth_date = models.DateField(null=True, blank=True)
    registration_source = models.CharField(max_length=20, choices=RegistrationSource.choices, default=RegistrationSource.LOCAL)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email

CONFIRMATION_CODE_TIME = 60 * 5
def confirmation_code_cache_key(user_id):
    return f"confirmation_code_{user_id}"
