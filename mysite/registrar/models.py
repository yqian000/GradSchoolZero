from django.db import models

# Create your models here.
class Taboo(models.Model):
    word=models.CharField(max_length=100, unique=True)
class Period(models.Model):
    is_class_setup=models.BooleanField(default=False,null=True)
    is_course_registration=models.BooleanField(default=False,null=True)
    is_class_running_period=models.BooleanField(default=False,null=True)
    is_grading_period=models.BooleanField(default=False,null=True)