from django.shortcuts import render

# Create your views here.
def instructorView(request):
	return render(request, "instructor/instructorView.html", {})

def accessCourse(request):
	return render(request, "instructor/accessCourse.html", {})

def assignGrade(request):
	return render(request, "instructor/assignGrade.html", {})

def complaintStudent(request):
	return render(request, "instructor/complaintStudent.html", {})

def viewWaitlist(request):
	return render(request, "instructor/viewWaitlist.html", {})
