from django.db import models

# Create your models here.
class Taboo(models.Model):
    word=models.CharField(max_length=100, unique=True)
class Period(models.Model):
    is_class_setup=models.BooleanField(default=False,null=True)
    is_course_registration=models.BooleanField(default=False,null=True)
    is_class_running_period=models.BooleanField(default=False,null=True)
    is_grading_period=models.BooleanField(default=False,null=True)
class upload_to_class_documents(models.Model):
    
      csv_file = models.FileField(upload_to='registrar/ClassDocuments/')

class Avalible_Courses(models.Model):
    course_name=models.CharField(max_length=200)
    start_time=models.CharField(max_length=200)
    section=models.CharField(max_length=200)
    end_time=models.CharField(max_length=200)
    max_size=models.PositiveSmallIntegerField(default=8) # upper limit


