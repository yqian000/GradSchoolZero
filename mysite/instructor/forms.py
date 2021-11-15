from django import forms
from django.contrib.auth import models
from django.forms import fields, ModelForm
from .models import *

class FileComplaintForm(ModelForm):
    complainee=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                'required':True,
                "placeholder":"John Doe"
            }
        ),label=" Complainee Name"
    )
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control'}),
        max_length=800,
        required=True)

    class Meta:
        model = InstructorComplaint
        fields = ['complainee', 'text']