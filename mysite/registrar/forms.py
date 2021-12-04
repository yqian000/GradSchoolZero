from django import forms
from django.db.models.fields import  BooleanField
from django.forms import fields, ModelForm
from django.forms.forms import Form
from account.models import Course
from student.models import StudentComplaint
from instructor.models import InstructorComplaint
from .models import *
import datetime
def yearcheck(p1):
	if p1!=int(datetime.datetime.now().year):
		raise forms.ValidationError("Acdeimic year is "+str(date.today().year))

	return p1

class ProcessStudentComplaintForm(ModelForm):

	class Meta:
		model = StudentComplaint
		labels = {
			"is_investigated": "By checking this box, I pledge my honor that I have investigated this complaint.",
			"person_id": "Person's ID: "
        }
		fields = ['is_investigated', 'action', 'punish_id']

class ProcessInstructorComplaintForm(ModelForm):

	class Meta:
		model = InstructorComplaint
		labels = {
			"is_investigated": "By checking this box, I pledge my honor that I have investigated this complaint.",
			"person_id": "Person's ID: "
        }
		fields = ['is_investigated', 'action', 'punish_id']

class TabooForm(ModelForm):

	class Meta:
		model = Taboo
		fields = '__all__'

class Periodsetup(ModelForm):
	is_class_setup=forms.BooleanField(label="class set up period",required=False)
	is_course_registration=forms.BooleanField(label="course registration",required=False)
	is_class_running_period=forms.BooleanField(label="class running period",required=False)
	is_grading_period=forms.BooleanField(label="grading class period",required=False)
	is_break_period=forms.BooleanField(label="post gra class period",required=False)

	class Meta:
		model = Period
		fields = '__all__'


class SetClassForm(ModelForm):
	class Meta:
		model = Course
		fields = ['instructor','meeting_date','max_size', 'is_open','start_time','end_time']