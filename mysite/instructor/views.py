from django.shortcuts import render
from .forms import *
from student.forms import FileComplaintForm
from student.models import Applcation

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
		form = FileComplaintForm(request.POST)

		if form.is_valid():
			form.save()
	
	form = FileComplaintForm()
	return render(request, "student/fileComplaint.html", {"form":form})

def viewWaitlist(request):
	return render(request, "instructor/viewWaitlist.html", {})
