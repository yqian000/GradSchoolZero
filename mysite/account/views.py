from django.shortcuts import render,redirect
from .forms import signupForm,ResetpasswordForm
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
from .models import User
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
            msg="Email address exists already or Non-CUNY email entered, try again please!"
            
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
            subject="Reset"
            message="Password has changed"
            email_from=settings.EMAIL_HOST_USER
            recipent_list=[email,]
            send_mail(subject,message,email_from,recipent_list)
            return  redirect("login")
        else:
            msg="something is wrong try it one more time"
            
    form=ResetpasswordForm()
    context={'form':form,"msg":msg}
    return render(request,"main/resetpassword.html",context)
'''def loginForm(request):
    msg=None
    if request.method=='POST':
        form=(request.POST)
        if form.is_valid():
            username=form.cleaned_date.get('username')
            password=form.cleaned_date.get('password')
            user=authenticate(username=username,password=password)
            login(request,user)
            return  redirect("home")
        else:
            msg="Email exist or None CUNY email entered, try again please!"
            
    form=signupForm()
    context={'form':form,"msg":msg}
    return render(request,"main/signup.html",context)
'''

