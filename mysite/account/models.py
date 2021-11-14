
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django.utils.translation import gettext_lazy
from django.core.exceptions import ValidationError
from django.contrib.auth.base_user import BaseUserManager
import django.utils.timezone
from django.conf import settings


def validate_mail(value):
    if "cuny.edu" in value:
        return value
    else:
        raise ValidationError("This field accepts mail id of CUNY only")
class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user=self.create_user(
            email = self.normalize_email(email),
            password=password,
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.set_password(password)
        user.save()
        return user

class User(AbstractUser,PermissionsMixin):
    email=models.EmailField(gettext_lazy('CUNY Email'),unique=True)
    username=models.CharField(max_length=200)
    first_name=models.CharField(max_length=150,blank="True")
    last_name=models.CharField(max_length=150,blank="True")
    last_login=models.DateTimeField(verbose_name="last login",auto_now=True)
    is_instructor=models.BooleanField('is instrutor',default=False)
    is_student=models.BooleanField('is student',default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) 
    is_admin = models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    First_login=models.BooleanField(default=True)
    object= CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

   

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    first_name=models.CharField(max_length=150,blank="True")
    last_name=models.CharField(max_length=150,blank="True")
    email=models.EmailField(gettext_lazy('email address'),unique=True,validators =[validate_mail])
    ID=models.PositiveIntegerField(default=0000000000)
    warning = models.PositiveSmallIntegerField(default=0) #[0, 32767]
    

class Instructor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    first_name=models.CharField(max_length=150,blank="True")
    last_name=models.CharField(max_length=150,blank="True")
    email=models.EmailField(gettext_lazy('email address'),unique=True,validators =[validate_mail])
    

