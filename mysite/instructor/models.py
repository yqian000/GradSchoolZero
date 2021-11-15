from django.db import models

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