
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import BooleanField

class User(AbstractUser):
    is_admin=BooleanField('Is admin',default=False)
    is_instructor=BooleanField('is instrutor',default=False)
    is_student=BooleanField('is student',default=False)