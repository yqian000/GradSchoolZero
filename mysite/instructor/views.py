from django.shortcuts import render
from .forms import *
from student.forms import FileComplaintForm

# Create your views here.
def instructorView(request):
	return render(request, "instructor/instructorView.html", {})

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
