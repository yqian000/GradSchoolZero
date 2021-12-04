from django.core.exceptions import ValidationError
from django.db import models
import datetime 

# Create your models here.
class Taboo(models.Model):
    word=models.CharField(max_length=100, unique=True)


TERM_CHOICES = (
    ('Spring', 'Spring'),
    ('Fall', 'Fall'),
    ('Summer', 'Summer'),
    ('Winter', 'Winter'),
  
)
def yearcheck(p1):
	if p1!=int(datetime.datetime.now().year):
		raise ValidationError("Acdeimic year is "+str(datetime.datetime.now().year))

	return p1


class Period(models.Model):
    is_class_setup=models.BooleanField(default=False,null=True)
    is_course_registration=models.BooleanField(default=False,null=True)
    is_class_running_period=models.BooleanField(default=False,null=True)
    is_grading_period=models.BooleanField(default=False,null=True)
    is_break_period=models.BooleanField(default=False,null=True)
    term_info = models.CharField(max_length=50, choices=TERM_CHOICES,null=True)
    year=models.IntegerField(validators=[yearcheck],null=True)
    