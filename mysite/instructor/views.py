from django.shortcuts import render
from .forms import *
from .models import *
from account.models import *
from student.models import Applcation
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def instructorView(request):
	if request.user.is_instructor:
		student_list = Applcation.objects.all()
		instructor = Instructor.objects.get(user=request.user)
		if instructor.warning == 3:
			instructor.is_suspended = True
			instructor.save()
		return render(request, "instructor/instructorView.html", {'student_list': student_list, 'i':instructor})
	else:
		return render(request, "main/forbidden.html",{})

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
