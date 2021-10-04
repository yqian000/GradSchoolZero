from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.forms.fields import EmailField
from .models import User
class LoginForm(forms.Form):
    username=EmailField(
        widget=forms.EmailInput(
            attrs={
                'unique':True,
                "class":"form-control",
                'required':True
            }
        )
    )
   
class signupForm(UserCreationForm):
    LastName=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                'required':True
            }
        )
    )
    FirstName=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                'required':True
            }
        )
    )
    password1=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                'required':True
            }
        )
    )
    password2=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                'required':True
            }
        )
    )
    Email=forms.CharField(
        widget=forms.TextInput(
            attrs={
              
                "class":"form-control",
                'required':True
            }
        )
    )
    class Meta:
        model=User
        fields=['FirstName','LastName','Email','password1','password2','is_admin','is_instructor','is_student']




    
