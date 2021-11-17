from django.shortcuts import render,redirect
from .forms import *
from .models import *
from account.models import *
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def studentView(request):
	if request.user.is_student:
		student = Student.objects.get(user=request.user)
		if student.warning == 3 and student.fine == 0:
			student.fine = 1 # set to has fine
			student.is_suspended = True
			student.save()

		return render(request, "student/studentView.html", {"s":student})
	else:
		return render(request, "main/forbidden.html",{})

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
		# create a new StudentComplaint model and set the ID and is_completed
		c = StudentComplaint(user_id=Student.objects.get(email=request.user.email).ID, is_completed=False)
		form = FileComplaintForm(request.POST, instance=c)

		if form.is_valid():
			form.save()
	
	form = FileComplaintForm()
	return render(request, "student/fileComplaint.html", {"form":form, "r":request})

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
	
def tutorial(request):
	return render(request, "student/tutorial.html", {})