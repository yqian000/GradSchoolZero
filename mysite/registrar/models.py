from django.db import models

# Create your models here.
STUDENT_COMPLAINT_CHOICES = (
	('ws', 'warn the student'),
	('wi', 'warn the instructor'),
)

INSTRUCTOR_COMPLAINT_CHOICES = (
	('ws', 'warn the student'),
	('ds', 'de-register the student'),
	('wi', 'warn the instructor'),
)

class ProcessStudentComplaint(models.Model):
    is_investigated = models.BooleanField(default=False)
    action = models.CharField(max_length=50, choices=STUDENT_COMPLAINT_CHOICES,default='ws')
    person_id = models.PositiveIntegerField()

class ProcessInstructorComplaint(models.Model):
    is_investigated = models.BooleanField(default=False)
    action = models.CharField(max_length=50, choices=INSTRUCTOR_COMPLAINT_CHOICES,default='ws')
    person_id = models.PositiveIntegerField()