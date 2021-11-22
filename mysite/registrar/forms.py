from django import forms
from django.db.models.fields import  BooleanField
from django.forms import fields, ModelForm
from django.forms.forms import Form
from .models import *
from student.models import StudentComplaint
from instructor.models import InstructorComplaint


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

class Periodsetup(forms.Form):
	is_class_setup=forms.BooleanField(label="calss set up period",required=False)
	is_course_registration=forms.BooleanField(label="courser registrtion",required=False)
	is_class_running_period=forms.BooleanField(label="class running period",required=False)
	is_grading_period=forms.BooleanField(label="grading class period",required=False)
	class Meta:
		model = Period
		fields = '__all__'

class read_class_form(forms.Form):

		csv=forms.FileField(label="Upload the class CSV",required=False)
