from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator
import jwt
from rest_framework_jwt.utils import jwt_payload_handler
from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
  
    first_name = models.CharField("First Name", max_length=128, blank=True)
    last_name = models.CharField("Last Name", max_length=128, blank=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
  
    email = models.EmailField("Email", unique=True)
    phone = models.CharField("Phone", max_length=17, validators=[
                             phone_regex], blank=True, null=True, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def create_jwt(self):
        """Function for creating JWT for Authentication Purpose"""
        payload = jwt_payload_handler(self)
        token = jwt.encode(payload, settings.SECRET_KEY)
        auth_token = token.decode('unicode_escape')
        return auth_token

    @property
    def is_admin(self):
        if self.user_type == 'admin':
            return True

        else:
            return False

class Location(models.Model):
    name = models.CharField("Name", max_length=512, blank=False)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'User Password Token'
        verbose_name_plural = 'User Password Token'

    def __str__(self):
        return self.token