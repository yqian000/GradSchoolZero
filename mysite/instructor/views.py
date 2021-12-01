from django.contrib import messages
from django.core import exceptions
from django.shortcuts import render,redirect

# from mysite import instructor
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
		if instructor.warning >= 3:
			instructor.is_suspanded = True
			instructor.save()
		return render(request, "instructor/instructorView.html", {'student_list': student_list, 'i':instructor})
	else:
		return render(request, "main/forbidden.html",{})

def accessCourse(request):
	if request.user.is_instructor:
		try:
			WL=Course.objects.filter(instructor=User.objects.get(email=request.user).id).order_by('name')
			return render(request, "instructor/accessCourse.html", {"WL":WL})
		except:
			return render(request, "instructor/accessCourse.html")
	else:
		return render(request, "main/forbidden.html",{})

def assignGrade(request):
	if request.user.is_instructor:
		return render(request, "instructor/assignGrade.html", {})
	else:
		return render(request, "main/forbidden.html",{})

def complaintStudent(request):
	if request.user.is_instructor:
		if request.method == "POST":
			# create a new InstructorComplaint model and set the ID and is_completed
			c = InstructorComplaint(user_id=Instructor.objects.get(email=request.user.email).ID, is_completed=False)
			form = FileComplaintForm(request.POST, instance=c)

			if form.is_valid():
				form.save()
		
		form = FileComplaintForm()
		return render(request, "instructor/fileComplaint.html", {"form":form, "r":request})

def viewWaitlist(request):
	if request.user.is_instructor:
		try:
			WL=course_record.objects.filter(waiting_list=True,Instructor_email=request.user).order_by('course_name')
			
			return render(request, "instructor/viewWaitlist.html", {"WL":WL})
		except:
			return render(request, "instructor/viewWaitlist.html", {"WL":WL})
	else:
		return render(request, "main/forbidden.html",{})

def JobApplication(request):
	if request.user.is_instructor:
		if request.method=="POST":
			form=jobForm(request.POST, request.FILES)
			application=career(email=request.POST['email'],firstname=request.POST['firstname'],lastname=request.POST['lastname'],Birthday=request.POST['Birthday'],salary_requirement=request.POST['salary_requirement'],phone=request.POST['phone'],startdate=request.POST['start_date'],work_experiences=request.POST['work_experience'],departments=request.POST['department'],resume=request.FILES['resume'], Portfolio_website=request.POST['Portfolio_website'])
			application.save()
			return redirect("home")
		else:
			form=jobForm()

		context={'form':form}
		return render(request,'instructor/job.html',context)
	else:
		return render(request, "main/forbidden.html",{})

def accept_waiting_list(request,pk=None):
	if request.user.is_instructor:
		try:
			c=course_record.objects.get(id=pk)
			c.waiting_list=False
			c.save()
			st=Student.objects.get(email=c.student_email)
			CR=Course.objects.get(name=c.course_name,instructor=Instructor.objects.get(email=c.Instructor_email))
			CR.curr_size+=1
			CR.save()
			st.course.add(CR)
			st.save()
			messages.success(request,"Successfully add students to the class")
			return redirect("viewWaitlist")
		except:
			messages.success(request,"Something seems wrong")
			return redirect("viewWaitlist")
	else:
		return render(request, "main/forbidden.html",{})


def reject_waiting_list(request,pk=None):
	if request.user.is_instructor:
		try:
			c=course_record.objects.get(id=pk)
			c.delete()
			messages.success(request,"Reject the enrollment for students in "+ c.course_name)
			return redirect("viewWaitlist")
		except:
			return redirect("viewWaitlist")
	else:
		return render(request, "main/forbidden.html",{})
