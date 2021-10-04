from django.shortcuts import render,redirect
from .forms import signupForm,LoginForm
# Create your views here.



def signup(request):
    if request.method=='POST':
        form=signupForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect("login")
    
    form=signupForm()
    context={'form':form}
    return render(request,"main/signup.html",context)


def login(request):
	return render(request, "main/login.html", {})