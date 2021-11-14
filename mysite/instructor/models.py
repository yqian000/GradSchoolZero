from django.db import models

# Create your models here.
class InstructorComplaint(models.Model):
    user_id = models.PositiveIntegerField() # hidden from user
    complainee = models.CharField(max_length=150)
    text = models.CharField(max_length=800)
    # hidden from user, should be set to true after registrar has reviewed it
    is_completed = models.BooleanField(default=False, blank=False) 

    def __str__(self):
        return self.complainee + ": " + self.text