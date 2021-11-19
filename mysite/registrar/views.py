
from django.shortcuts import render,redirect
from student.models import *
from instructor.models import *
from account.models import *
from django.core.mail import send_mail
from django.conf import settings
from .forms import *
from .models import *
from django.contrib import messages


# Create your views here.
def registrarView(request):
	return render(request, "registrar/registrarView.html", {})

def viewNewUser(request):
	try:
		user=User.objects.filter(email=request.user)
	except:
		return render(request, "main/forbidden.html",{})
	if  user[0].is_admin==True:
		application=Applcation.objects.all()
		jobs=career.objects.all()
		context={'application':application,'jobs':jobs}
		return render(request, "registrar/viewNewUser.html",context)
	else:
		return render(request, "main/forbidden.html",{})

def viewGrad(request):
	return render(request, "registrar/viewGrad.html", {})

def viewRating(request):
	return render(request, "registrar/viewRating.html", {})

def setClass(request):
	return render(request, "registrar/setClass.html", {})

def tabooList(request):
	if request.method == "POST":
		form = TabooForm(request.POST)
		if form.is_valid():
			form.save()

	taboo = Taboo.objects.all()
	form = TabooForm()
	return render(request, "registrar/tabooList.html", {"form":form, "taboo":taboo})

def processStudentComplaint(request, pk=None):
	if request.method == "POST":
		# get the corresponding complaint
		c = StudentComplaint.objects.get(id=pk)

		form = ProcessStudentComplaintForm(request.POST, instance=c)

		if form.is_valid():
			form.save()
			# mark is as completed
			res = StudentComplaint.objects.get(id=pk)
			res.is_completed = True
			res.save()

			# process actions: 
			# warn the student
			if res.action == "ws":
				s = Student.objects.get(ID=res.punish_id)
				s.warning += 1
				s.save()
			# warn the instructor
			elif res.action == "wi":
				i = Instructor.objects.get(ID=res.punish_id)
				i.warning += 1
				i.save()

			scomplaint = StudentComplaint.objects.all()
			icomplaint = InstructorComplaint.objects.all()
			return render(request, "registrar/manageComplaint.html", {"sc": scomplaint, "ic": icomplaint})

	form = ProcessStudentComplaintForm()
	return render(request, "registrar/processStudentComplaint.html", {"form":form})

def processInstructorComplaint(request, pk=None):
	if request.method == "POST":
		c = InstructorComplaint.objects.get(id=pk)

		form = ProcessInstructorComplaintForm(request.POST, instance=c)

		if form.is_valid():
			form.save()
			# mark is as completed
			res = InstructorComplaint.objects.get(id=pk)
			res.is_completed = True
			res.save()

			# process actions
			# warn the student
			if res.action == "ws":
				s = Student.objects.get(ID=res.punish_id)
				s.warning += 1
				s.save()
			# warn the instructor
			elif res.action == "wi":
				i = Instructor.objects.get(ID=res.punish_id)
				i.warning += 1
				i.save()
			elif res.action == "ds":
				s = Student.objects.get(ID=res.punish_id)
				s.is_suspended = True
				s.save()

			scomplaint = StudentComplaint.objects.all()
			icomplaint = InstructorComplaint.objects.all()
			return render(request, "registrar/manageComplaint.html", {"sc": scomplaint, "ic": icomplaint})

	form = ProcessInstructorComplaintForm()
	return render(request, "registrar/processInstructorComplaint.html", {"form":form})

def manageComplaint(request):
	scomplaint = StudentComplaint.objects.all()
	icomplaint = InstructorComplaint.objects.all()
	return render(request, "registrar/manageComplaint.html", {"sc": scomplaint, "ic": icomplaint})

def manageSuspension(request):
	return render(request, "registrar/manageSuspension.html", {})

def rejectapplications(request,pk=None):
	try:
		if Applcation.objects.get(id=pk)!=None:
			if  float(Applcation.objects.get(id=pk).Gpa)<3:
				Applcation.objects.get(id=pk).delete()
				return redirect("viewNewUser")

			else:
				Applcation.objects.get(id=pk).delete()
				return render(request,"registrar/reasonform.html")
	except:
			
		return redirect("viewNewUser")

def acceptapplications(request,pk=None):
	
	try:
			if  float(Applcation.objects.get(id=pk).Gpa)>3:
				user=User.objects.last()
				StudentEmail=Applcation.objects.get(id=pk).firstname[0]+Applcation.objects.get(id=pk).lastname+"00"+str(int(user.id)+1)+"@citymail.cuny.edu"
				user=User(email=StudentEmail,username=StudentEmail,first_name=Applcation.objects.get(id=pk).firstname,last_name=Applcation.objects.get(id=pk).lastname,is_student=True,First_login=True)
				user.set_password(StudentEmail)
				user.save()
				ID=20000000+int(user.id)+1
				student=Student(email=StudentEmail,first_name=Applcation.objects.get(id=pk).firstname,last_name=Applcation.objects.get(id=pk).lastname,ID=ID)
				student.save()
				try:
					subject="Congratulations"
					message="Thank you for applying CUNY.After deep consideration, we decide to give you the offer, your CUNY email will be .., and login password will be same."
					email_from=settings.EMAIL_HOST_USER
					recipent_list=[Applcation.objects.get(id=pk).email]
					send_mail(subject,message,email_from,recipent_list)
				except:
					print("hello")

				Applcation.objects.get(id=pk).delete()
				return redirect("viewNewUser")

			else:
				Applcation.objects.get(id=pk).delete()
				return render(request,"registrar/reasonform.html")

	
	except:
			
			return redirect("viewNewUser")

def reject_job_application(request,pk=None):
	try:
		if career.objects.get(id=pk)!=None:


				try:
					subject="Sorry"
					message="We appreciate your interest in CUNY and the time you’ve invested in applying for instructor role. There has been significant interest in this role At this time, we have made the decision to move forward with other applicants."
					email_from=settings.EMAIL_HOST_USER
					recipent_list=[career.objects.get(id=pk).email]
					send_mail(subject,message,email_from,recipent_list)
				except:
					pass
			
				career.objects.get(id=pk).delete()
				return redirect("viewNewUser")
	except:
			
		return redirect("viewNewUser")

def accept_job_applications(request,pk=None):
	
	try:
			if career.objects.get(id=pk)!=None:
				user=User.objects.last()
				ProfesorEmail=career.objects.get(id=pk).firstname[0]+career.objects.get(id=pk).lastname+"00"+str(int(user.id)+1)+"@citymail.cuny.edu"
				user=User(email=ProfesorEmail,username=ProfesorEmail,first_name=career.objects.get(id=pk).firstname,last_name=career.objects.get(id=pk).lastname,is_instructor=True,First_login=True)
				user.set_password(ProfesorEmail)
				user.save()
				ID=10000000+int(user.id)+1
				instructor=Instructor(email=ProfesorEmail,first_name=career.objects.get(id=pk).firstname,last_name=career.objects.get(id=pk).lastname,ID=ID)
				instructor.save()
				try:
					subject="Congratulations"
					message="Thank you for applying CUNY.After deep consideration, we decide to give you the offer, your CUNY email will be .., and login password will be same."
					email_from=settings.EMAIL_HOST_USER
					recipent_list=[career.objects.get(id=pk).email]
					send_mail(subject,message,email_from,recipent_list)
				except:
					pass

				career.objects.get(id=pk).delete()
				return redirect("viewNewUser")

	
	except:
			
			return redirect("viewNewUser")
def PeriodSetup(request):
	if request.method=='POST':
		form=Periodsetup(request.POST)
		period=Period.objects.last()
		

		class_setup=request.POST.get('is_class_setup')
		course_registration=request.POST.get('is_course_registration')
		class_running_period=request.POST.get('is_class_running_period')
		grading_period=request.POST.get('is_grading_period')
		if class_setup=='on':
			period.is_class_setup=True
		if course_registration =='on':
			period.is_course_registration=True
		if class_running_period=='on':
			period.is_class_running_period=True
		if 	grading_period=='on':
			period.is_grading_period=True
		period.save()
		messages.success(request, 'Period set up successful')
		return render(request, "registrar/periodsetup.html", {"form":form})
	else :
		form=Periodsetup()
		return render(request, "registrar/periodsetup.html", {"form":form})




	

