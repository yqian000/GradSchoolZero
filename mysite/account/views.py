from django import forms
from django.core.checks import messages
from django.shortcuts import render,redirect
from .forms import loginForm, signupForm,ResetpasswordForm
from django.core.mail import send_mail
from django.conf import settings
from .models import User
from django.contrib.auth import authenticate,login
from django.forms import fields,ValidationError
# Create your views here.



def signup(request):
    msg=None
    if request.method=='POST':
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']

        form=signupForm(request.POST)
        if form.is_valid():
            form.save()
            subject="Welcome"
            message="Hi, %s %s \n weclome to CUNY"%(firstname,lastname)
            email_from=settings.EMAIL_HOST_USER
            recipent_list=[email,]
            send_mail(subject,message,email_from,recipent_list)
            return  redirect("login")
        else:
            context={'form':form}
            return render(request,"main/signup.html",context)
            
    form=signupForm()
    context={'form':form,"msg":msg}
    return render(request,"main/signup.html",context)
def resetpassword(request):
    msg=None
    if request.method=='POST':
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        form=ResetpasswordForm(request.POST)
        if form.is_valid():
            u = User.objects.get(email=email)
            u.set_password(password1)
            u.save()
            try: 
                subject="Reset"
                message="Password has changed"
                email_from=settings.EMAIL_HOST_USER
                recipent_list=[email,]
                send_mail(subject,message,email_from,recipent_list)
                return  redirect("login")
            except:
                return  redirect("login")
        else:
            context={'form':form}
            return render(request,"main/resetpassword.html",context)
            
    form=ResetpasswordForm()
    context={'form':form,"msg":msg}
    return render(request,"main/resetpassword.html",context)

def login_view(request):
        message=None
        if request.method=='POST':
           

            try:
                email=request.POST['username']
                user=User.objects.get(email=email)
            except:
                message="CUNY EMAIL DOES NOT EXIST"
                form=loginForm()
                context={'form':form,"msg":message}
                return render(request,"main/login.html",context)
            

            email=request.POST['username']
            user=User.objects.get(email=email)
            if  user.First_login and user.is_admin==False:
                return redirect("reset")
            form=loginForm(request.POST)
            if form.is_valid():
                username=email
                password=request.POST['password']
                user=authenticate(username=username,password=password)
            
                if user is not None:
                  
                    login(request,user)
                    user.First_login=False
                    user.save
                    if user.is_admin:
                        return redirect("registrarView")
                    elif user.is_student:
                        return  redirect("studentView")
                    else:
                        return  redirect("home")

                else:
                    message="Credentials are not correct, please try one more time" 
             
            
        form=loginForm()
        context={'form':form,"msg":message}
        return render(request,"main/login.html",context)

