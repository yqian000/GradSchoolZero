from django.db import models
from django.utils.regex_helper import flatten_result

# Create your models here.

INSTRUCTOR_COMPLAINT_CHOICES = (
    ('init', 'Select an option'),
    ('ws', 'warn the student'),
    ('ds', 'de-register the student'),
    ('wi', 'warn the instructor'),
)

class InstructorComplaint(models.Model):
    user_id = models.PositiveIntegerField() # hidden from user
    complainee = models.CharField(max_length=150)
    text = models.CharField(max_length=800)
    # hidden from user, should be set to true after registrar has reviewed it
    is_completed = models.BooleanField(default=False, blank=False) 
    # only registrar can view the following
    is_investigated = models.BooleanField(default=False)
    action = models.CharField(max_length=50, choices=INSTRUCTOR_COMPLAINT_CHOICES,default='init')
    punish_id = models.PositiveIntegerField(default=00000000)

    def __str__(self):
        return self.complainee + ": " + self.text

class career(models.Model):
    email=models.EmailField()
    firstname=models.CharField(max_length=150,blank="True")
    lastname=models.CharField(max_length=150,blank="True")
    startdate=models.DateField(default="0000-00-00")
    Portfolio_website=models.CharField(max_length=250)
    Birthday=models.DateField(default="0000-00-00")
    salary_requirement=models.CharField(max_length=250)
    phone= models.CharField(max_length=60, default="")
    resume= models.FileField(upload_to='instructor/documents/')
    departments=models.CharField(max_length=150,blank="True")
    work_experiences=models.CharField(max_length=200,blank="True")
    def __str__(self):
        return self.firstname + ' ' + self.lastname