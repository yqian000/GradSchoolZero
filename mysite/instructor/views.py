from django.contrib import messages
from django.core import exceptions
from django.shortcuts import render,redirect

from decimal import Decimal
from .forms import *
from .models import *
from account.models import *
from student.models import Applcation
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def instructorView(request):
	if request.user.is_instructor:
		courses = course_record.objects.filter(Instructor_email=request.user.email,grade=None)
		students = Student.objects.all()
		for course in courses:
			students = students.union(Student.objects.filter(email=course.student_email))
		instructor = Instructor.objects.get(user=request.user)
		period = Period.objects.last()
		p = ''
		if period.is_class_setup:
			p = 'class setup period'
		elif period.is_course_registration:
			p = 'course registration period'
		elif period.is_class_running_period:
			p = 'class running period'
		elif period.is_grading_period:
			p = 'grading period'
		elif period.is_break_period:
			p ='break period'
		if instructor.warning >= 3:
			instructor.is_suspanded = True
			instructor.save()
		return render(request, "instructor/instructorView.html", {'student_list': students, 'i':instructor, 'p':p})
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
	if request.user.is_instructor :
		if   Period.is_grading_period:
			
				
				
				WL=course_record.objects.filter(Instructor_email=request.user,grade="").order_by('course_name')
		
				
				return render(request, "instructor/assignGrade.html", {"WL":WL})
			
		else:


				messages.success(request,"visit the grading page during grading period")
				return render(request, "instructor/assignGrade.html")
				
			
	else:
		return render(request, "main/forbidden.html",{})
def grade(request,pk=None):
		if request.user.is_instructor :
			if request.method == "POST" and Period.objects.last().is_grading_period:

				c=course_record.objects.get(id=pk)
				form=gradeform(request.POST,instance=c)
				student=Student.objects.get(email=c.student_email)

				form.save()
				try:
					course=Course.objects.get(name=c.course_name,semester=c.semester,instructor=User.objects.get(email=request.user).id)
					overal_gpa=course_record.objects.filter(course_name=course.name,semester=course.semester,Instructor_email=request.user)
					Gpa=0
					for i in overal_gpa:
						if i.grade=="A":
							Gpa+=4
						elif i.grade=="B":
							Gpa+=3.5
						elif i.grade=='C':
							Gpa+=3
						elif i.grade=='D':
							Gpa+=2.5
						elif i.grade=='F' or i.grade=="W":
							Gpa+=0
				
					course.gpa=Gpa/len(overal_gpa)
					course.save()
				except:
					pass
				GPA=course_record.objects.filter(student_email=student.email).all().exclude(grade="")
					
				if c.grade=="A":
						student.GPA=(student.GPA+4)/len(GPA)
						student.save()
				elif c.grade=="B":
						student.GPA=(student.GPA+Decimal(3.5))/len(GPA)
						student.save()
				elif c.grade=='C':
						student.GPA=(student.GPA+3)/len(GPA)
						student.save()
				elif c.grade=='D':
						student.GPA=(student.GPA+Decimal(2.5))/len(GPA)
						student.save()
				elif c.grade=='F' or c.grade=="W":
						student.GPA=(student.GPA+0)/len(GPA)
						student.save()
				
				course=course_record.objects.filter(course_name=c.course_name,grade="F",student_email=student.email)
				if(len(course)>=2):
					student.is_suspanded=True
				student.save()

				if student.GPA<=2.5:
					try:
						subject="Warning"
						message="You need to make an appointment with registrar about your gpa" 
						email_from=settings.EMAIL_HOST_USER
						recipent_list=[student.email]
						send_mail(subject,message,email_from,recipent_list)
					except:
						pass

				return redirect("assignGrade")
			else:
				c=course_record.objects.get(id=pk)
				student=Student.objects.get(email=c.student_email)
				form=gradeform()
				
				return render(request, "instructor/processgrade.html",{"s":student,"form":form,"c":c})
			
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
	if request.method=="POST":
		form=jobForm(request.POST, request.FILES)
		application=career(email=request.POST['email'],firstname=request.POST['firstname'],lastname=request.POST['lastname'],Birthday=request.POST['Birthday'],salary_requirement=request.POST['salary_requirement'],phone=request.POST['phone'],startdate=request.POST['start_date'],work_experiences=request.POST['work_experience'],departments=request.POST['department'],resume=request.FILES['resume'], Portfolio_website=request.POST['Portfolio_website'])
		application.save()
		return redirect("home")
	else:
		form=jobForm()

	context={'form':form}
	return render(request,'instructor/job.html',context)

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
			try:
					subject="Regarding"+ c.course_name+" waiting list"
					message="you're granted the permission for enrollment for"+c.course_name
					email_from=settings.EMAIL_HOST_USER
					recipent_list=[c.student_email]
					send_mail(subject,message,email_from,recipent_list)
			except:
					pass
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
			try:
					subject="sorry"
					message=c.course_name+"is closed,you are not granted the permission for the classes"
					email_from=settings.EMAIL_HOST_USER
					recipent_list=[c.student_email]
					send_mail(subject,message,email_from,recipent_list)
			except:
					pass
			return redirect("viewWaitlist")
		except:
			return redirect("viewWaitlist")
	else:
		return render(request, "main/forbidden.html",{})

