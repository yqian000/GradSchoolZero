from django.shortcuts import render
from .forms import *
from .models import *
from account.models import *
from student.models import Applcation
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def instructorView(request):
	student_list = Applcation.objects.all()
	return render(request, "instructor/instructorView.html", 
		{'student_list': student_list})

def accessCourse(request):
	return render(request, "instructor/accessCourse.html", {})

def assignGrade(request):
	return render(request, "instructor/assignGrade.html", {})

def complaintStudent(request):
	if request.method == "POST":
		# create a new InstructorComplaint model and set the ID and is_completed
		c = InstructorComplaint(user_id=Instructor.objects.get(email=request.user.email).ID, is_completed=False)
		form = FileComplaintForm(request.POST, instance=c)

		if form.is_valid():
			form.save()
	
	form = FileComplaintForm()
	return render(request, "instructor/fileComplaint.html", {"form":form, "r":request})

def viewWaitlist(request):
	return render(request, "instructor/viewWaitlist.html", {})
