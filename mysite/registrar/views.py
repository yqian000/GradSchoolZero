
from django.shortcuts import render,redirect
from student.models import *
from instructor.models import *
from account.models import *
from registrar.models import *
from django.core.mail import send_mail
from django.conf import settings
from .forms import *



# Create your views here.
def registrarView(request):
	return render(request, "registrar/registrarView.html", {})

def viewNewUser(request):
	user=User.objects.filter(email=request.user)
	if  user[0].is_admin==True:
		application=Applcation.objects.all()
		context={'application':application}
		return render(request, "registrar/viewNewUser.html",context)
	else:
		return render(request, "registrar/forbidden.html",{})

def viewGrad(request):
	return render(request, "registrar/viewGrad.html", {})

def viewRating(request):
	return render(request, "registrar/viewRating.html", {})

def setClass(request):
	return render(request, "registrar/setClass.html", {})

def processComplaint(request):
	if request.method == "POST":
		form = ProcessStudentComplaintForm(request.POST)

		if form.is_valid():
			form.save()
	# generate warnings ...
	
	form = ProcessStudentComplaintForm()
	return render(request, "registrar/processComplaint.html", {"form":form})

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
				student=Student(email=StudentEmail,first_name=Applcation.objects.get(id=pk).firstname,last_name=Applcation.objects.get(id=pk).lastname)
				student.save()
				try:
					subject="Congratulations"
					message="Thank you for applying CUNY.After deep consideration, we decide to give you the offer, your CUNY email will be %s, and login password will be same."
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
	

	
	
	

