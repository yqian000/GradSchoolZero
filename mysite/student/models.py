from django.db import models
from django.db.models.fields.related import OneToOneField
from django.forms.fields import EmailField
from account.models import *



class Applcation(models.Model):
    email=models.EmailField()
    firstname=models.CharField(max_length=150,blank="True")
    lastname=models.CharField(max_length=150,blank="True")
    Gpa=models.CharField(max_length=150,blank="True")
    semester=models.CharField(max_length=150,blank="True")
    Birthday=models.DateField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60, default="NewYork")
    state = models.CharField(max_length=30, default="NewYork")
    zip = models.CharField(max_length=5, default="11220")
    country = models.CharField(max_length=50)
    transcprit= models.FileField(upload_to='student/documents/')
    letters= models.FileField(upload_to='student/documents/')
    personal_statement = models.FileField(upload_to='student/documents/')
    major=models.CharField(max_length=150,blank="True")
    def __str__(self):
        return self.firstname + ' ' + self.lastname

STUDENT_COMPLAINT_CHOICES = (
    ('init', 'Select an option'),
    ('ws', 'warn the student'),
    ('wi', 'warn the instructor'),
)

class StudentComplaint(models.Model):
    user_id = models.PositiveIntegerField() # hidden from user
    complainee = models.CharField(max_length=150)
    text = models.CharField(max_length=800)
    # hidden from user, should be set to true after registrar has reviewed it
    is_completed = models.BooleanField(default=False, blank=False) 
    # only registrar can view the following
    is_investigated = models.BooleanField(default=False)
    action = models.CharField(max_length=50, choices=STUDENT_COMPLAINT_CHOICES,default='init')
    punish_id = models.PositiveIntegerField(default=00000000)

    def __str__(self):
        return self.complainee + ": " + self.text

STAR_CHOICES = (
    ('1', '1 star'),
    ('2', '2 stars'),
    ('3', '3 stars'),
    ('4', '4 stars'),
    ('5', '5 stars'),
)

COURSE_CHOICES = (
    ('Programming Languages', 'Programming Languages'),
    ('Advanced Data Structures', 'Advanced Data Structures'),
    ('Advanced Algorithms', 'Advanced Algorithms'),
    ('Software Engineering', 'Software Engineering'),
    ('Operating Systems', 'Operating Systems'),
    ('Computer Systems', 'Computer Systems'),
    ('Computer Security', 'Computer Security'),
    ('Machine Learning', 'Machine Learning'),
    ('Data Science', 'Data Science'),
    ('English', 'English'),
)

class RateClass(models.Model):
    email = models.EmailField()
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    star = models.CharField(max_length=50, choices=STAR_CHOICES)
    review = models.CharField(max_length=800)

class DropClass(models.Model):
    email = models.EmailField()
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)

    
class Cart(models.Model):
        CourseID=models.IntegerField(blank=True)
        Email=models.EmailField(blank=True)