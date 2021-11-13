from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm
from django.forms import fields,ValidationError
from django.forms.fields import EmailField
from .models import User
from django.contrib.auth import authenticate,password_validation



def LOGIN(self,username,password):
        user=authenticate(username=username,password=password)
            
        if user is None:
                raise forms.ValidationError("please input correct CUNY credentials")
        
def validate_mail(value):
        if "cuny.edu" in value.lower():
            return value.lower()
        else:
            raise ValidationError("This field accepts mail id of CUNY only")


def clean_new_password1(password1):   

        MIN_LENGTH=8
        # At least MIN_LENGTH long
        if len(password1) <MIN_LENGTH:
            raise forms.ValidationError("The new password must be at least %d characters long." % self.MIN_LENGTH)

        # At least one letter and one non-letter
        first_isalpha = password1[0].isalpha()
        if all(c.isalpha() == first_isalpha for c in password1):
            raise forms.ValidationError("The new password must contain at least one letter and at least one digit or" \
                                        " punctuation character.")
        return password1
class signupForm(UserCreationForm):

    
    last_name=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                'required':True
            }
        )
    )
    first_name=forms.CharField(
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
        ),validators =[clean_new_password1]
    )
    
    password2=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                'required':True
            }
        ),validators =[clean_new_password1])

     
    email=forms.CharField(
        widget=forms.TextInput(
            attrs={
              
                "class":"form-control",
                'required':True
            }
        ),validators =[validate_mail]
    )

    
    class Meta:
        model=User
        fields=['first_name','last_name','email','password1','password2','is_instructor','is_student']

class loginForm(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                'required':True
            }
        )
    )
    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                'required':True
            }
        ),help_text= ('<div  style="font-weight: bold;" class="alert alert-warning alert-dismissible fade show" role="alert"><strong>if you are first time log in, you will be redirected to resetpassword page!!</strong></div>')
    )
    
    class Meta:
        model=User
        fields=['email',"password"]
    
  
            
class ResetpasswordForm(PasswordResetForm):
    email=forms.CharField(
        widget=forms.TextInput(
            attrs={
              
                "class":"form-control",
                'required':True
            }
        ),validators =[validate_mail]
    )
    password1=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                'required':True
            }
        ),validators =[clean_new_password1]
    )
    password2=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                'required':True
            }
        ),label='Confirm Password',validators =[clean_new_password1]
    )

    class Meta:
        model=User
        fields=['email','password1','password2']
   

    