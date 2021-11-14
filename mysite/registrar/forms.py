from django import forms
from django.forms import fields, ModelForm
from .models import *

class ProcessStudentComplaintForm(ModelForm):

	class Meta:
		model = ProcessStudentComplaint
		labels = {
			"is_investigated": "By checking this box, I pledge my honor that I have investigated this complaint.",
			"person_id": "Person's ID: "
        }
		fields = '__all__'

class ProcessInstructorComplaint(ModelForm):

	class Meta:
		model = ProcessInstructorComplaint
		labels = {
			"is_investigated": "By checking this box, I pledge my honor that I have investigated this complaint.",
			"person_id": "Person's ID: "
        }
		fields = '__all__'