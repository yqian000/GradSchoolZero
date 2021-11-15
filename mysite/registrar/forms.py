from django import forms
from django.forms import fields, ModelForm
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