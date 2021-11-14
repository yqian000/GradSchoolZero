from django.shortcuts import render,redirect
from .forms import *
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def studentView(request):
	return render(request, "student/studentView.html", {})

def rateClass(request):
	if request.method == "POST":
		form = RateClassForm(request.POST)

		if form.is_valid():
			form.save()
	else:
		form = RateClassForm()
	return render(request, "student/rateClass.html", {"form":form})

def fileComplaint(request):
	if request.method == "POST":
		form = FileComplaintForm(request.POST)

		if form.is_valid():
			form.save()
	
	form = FileComplaintForm()
	return render(request, "student/fileComplaint.html", {"form":form})

def viewWarning(request):
	return render(request, "student/viewWarning.html", {})

def Application(request):
	if request.method=="POST":
		form=applicationForm(request.POST, request.FILES)
			
		application=Applcation(email=request.POST['email'],firstname=request.POST['firstname'],lastname=request.POST['lastname'],Gpa=request.POST['Gpa'],semester=request.POST['semester'],Birthday=request.POST['Birthday'],address=request.POST['address'],city=request.POST['city'],state=request.POST['state'],zip=request.POST['zip'],country=request.POST['country'],letters=request.FILES["letters"],personal_statement=request.FILES['personal_statement'],major=request.POST['Major'],transcprit=request.FILES['transcprit'])
		application.save()
		return redirect("home")
	else:
		form=applicationForm()

	context={'form':form}
	return render(request,'main/admission.html',context)
	
     
            
    