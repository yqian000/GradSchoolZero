
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django.db.models.base import Model
from django.forms.fields import CharField
from django.utils.translation import gettext_lazy
from django.core.exceptions import ValidationError
from django.contrib.auth.base_user import BaseUserManager
import django.utils.timezone
from django.conf import settings
from student.models import *


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

    def __str__(self):
        return self.email
class Instructor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    first_name=models.CharField(max_length=150,blank="True")
    last_name=models.CharField(max_length=150,blank="True")
    email=models.EmailField(gettext_lazy('email address'),unique=True,validators =[validate_mail])
    ID=models.PositiveIntegerField(default=00000000)
    warning = models.PositiveSmallIntegerField(default=0) #[0, 32767]
    is_warned=models.BooleanField(default=False)
    is_suspanded=models.BooleanField(default=False)
    is_working=models.BooleanField(default=True)
    is_suspanded=models.BooleanField(default=False)
    is_working=models.BooleanField(default=False)

    def __str__(self):
        return self.email
class Course(models.Model):
    name=models.CharField(max_length=200)
    instructor=models.ForeignKey(Instructor,on_delete=models.CASCADE,blank=True,null=True)
    meeting_date=models.CharField(max_length=200,null=True,blank=True)
    curr_size=models.PositiveSmallIntegerField(default=0) # number of students in class
    max_size=models.PositiveSmallIntegerField(default=8) # upper limit
    is_open=models.BooleanField(default=False) # closed or cancelled class will be False
    is_dropped=models.BooleanField(default=False)
    start_time=models.CharField(max_length=5,null=True,blank=True)
    end_time=models.CharField(max_length=5,null=True,blank=True)
    rate=models.DecimalField(max_digits=3,decimal_places=2)
    grade=models.CharField(max_length=1,blank=True,null=True)

    def __str__(self):
        return self.name
class course_record(models.Model):
    course_name=models.CharField(blank=True,max_length=200)
    student_email=models.EmailField(blank=True)
    Instructor_email=models.EmailField(blank=True)
    semster=models.CharField(blank=True,max_length=20)
    grade=models.CharField(blank=True,max_length=3)
    waiting_list=models.BooleanField(default=False)
    

class Student(models.Model):
   
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    cr=models.OneToOneField(course_record,on_delete=models.SET_NULL,blank=True,null=True)
    first_name=models.CharField(max_length=150,blank="True")
    last_name=models.CharField(max_length=150,blank="True")
    email=models.EmailField(gettext_lazy('CUNY Email'),unique=True)
    ID=models.PositiveIntegerField(default=0)
    warning = models.PositiveSmallIntegerField(default=0) #[0, 32767]
    is_warned=models.BooleanField(default=False)
    GPA=models.IntegerField(default=0)
    is_suspanded=models.BooleanField(default=False)
    is_graduate=models.BooleanField(default=False)
    credit=models.PositiveSmallIntegerField(default=0) #[0, 32767]
    fine=models.PositiveSmallIntegerField(default=0) # 0->no fine; 1->has fine; 2->fine received
    is_special_assigned=models.BooleanField(default=False,null=True,blank=True)
    course=models.ManyToManyField(Course,blank=True)

    def __str__(self):
        return self.email


    
