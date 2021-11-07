from django import forms
from .models import Application


class RateClassForm(forms.Form):
    course = forms.CharField(label = "Select a course: ", required = True)
    star = forms.IntegerField(label =" Assign Stars (1 worst to 5 best): ", required = True)
    review = forms.CharField(widget = forms.Textarea, required = True)

class FileComplaintForm(forms.Form):
    name = forms.CharField(max_length = 60, required = True)
<<<<<<< HEAD
    reason = forms.CharField(widget = forms.Textarea, required = True)

class ApplicationForm(forms.Form):
    email=forms.CharField(
        widget=forms.TextInput(
            attrs={
              
                "class":"form-control",
                'required':True,
                "placeholder":"Email"
            }
        )
    )
    firstname=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-group col-md-6",
                "class":"form-control",
                'required':True,
                "placeholder":"First Name"
                
            }
        ),label=" First Name"
    )
    lastname=forms.CharField(
        widget=forms.TextInput(
            attrs={

                "class":"form-group col-md-6",
                "class":"form-control",
                'required':True,
                "placeholder":"Last Name"
                
            }
        ),label=" Last Name"
    )
    gpa=forms.CharField(
        widget=forms.TextInput(
            attrs={
              
                "class":"form-control",
                'required':True,
                "placeholder":"x.xx"
                
            }
        ),label="GPA"
    )
    semester=forms.CharField(
        widget=forms.TextInput(
            attrs={
              
                "class":"form-control",
                'required':True,
                "placeholder":"spring 2021"
                
            }
        ),label="Semester"
    )
    birthday = forms.DateField(widget=forms.DateInput(attrs=
                                {
                                    'class': 'form-control datetimepicker-input',
                                    'data-target': '#datetimepicker1',
                                    "placeholder":"YYYY-MM-DD"
                                }))
    address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        max_length=300,
        required=True)
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True)
    state = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True)
    country = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True)
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True)
    zip = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True)
    transcript = forms.FileField(label="transcript",required=True)
    letters = forms.FileField(label="recommandation letter",required=True)
    personal_statement = forms.FileField(label="personal statement",required=True)
    major = forms.CharField(
        widget=forms.TextInput(
            attrs={
              
                "class":"form-control",
                'required':True,
                "placeholder":"Computer Science"
                
            }
        ),label="Major"
    )

    class Meta:
        model=Application
        fields=['email',"firstname","lastname","Gpa","semester","Birthday","address","city","state","country","phone","zip","transcript","letters","personal_statement","Major"]


=======
    reason = forms.CharField(widget = forms.Textarea, required = True)
>>>>>>> parent of d70f5b3 (prototype of admission table database and form)