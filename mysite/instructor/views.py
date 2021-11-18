from django.shortcuts import render,redirect
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


def JobApplication(request):
	if request.method=="POST":
		form=jobForm(request.POST, request.FILES)
		application=career(email=request.POST['email'],firstname=request.POST['firstname'],lastname=request.POST['lastname'],Birthday=request.POST['Birthday'],salary_requirement=request.POST['salary_requirement'],phone=request.POST['phone'],startdate=request.POST['start_date'],work_experiences=request.POST['work_experience'],departments=request.POST['department'],resume=request.FILES['resume'], Portfolio_website=request.POST['Portfolio_website'])
		application.save()
		return redirect("home")
	else:
		form=jobForm()

	context={'form':form}
	return render(request,'instructor/job.html',context)
