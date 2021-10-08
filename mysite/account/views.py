from django.shortcuts import render,redirect
from .forms import signupForm
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
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
            msg="Email address exists or None CUNY email entered, try again please!"
            
    form=signupForm()
    context={'form':form,"msg":msg}
    return render(request,"main/signup.html",context)
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

