<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> parent of e150cc2 (Merge pull request #7 from yqian000/addUser)
=======
>>>>>>> parent of e2cf0a5 (Fix typos and html styling.)
<<<<<<< Updated upstream
from django.shortcuts import render
from .forms import RateClassForm, FileComplaintForm
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> parent of e2cf0a5 (Fix typos and html styling.)
=======
>>>>>>> parent of e150cc2 (Merge pull request #7 from yqian000/addUser)
=======
>>>>>>> parent of e2cf0a5 (Fix typos and html styling.)

from django.shortcuts import render,redirect
from .forms import *

from django.core.mail import send_mail
from django.conf import settings

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

from django.shortcuts import render
from .forms import RateClassForm, FileComplaintForm

=======
=======
>>>>>>> parent of e150cc2 (Merge pull request #7 from yqian000/addUser)
=======
>>>>>>> parent of e2cf0a5 (Fix typos and html styling.)
from django.shortcuts import render
from .forms import RateClassForm, FileComplaintForm

>>>>>>> Stashed changes
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> parent of e2cf0a5 (Fix typos and html styling.)
=======
>>>>>>> parent of e150cc2 (Merge pull request #7 from yqian000/addUser)
=======
>>>>>>> parent of e2cf0a5 (Fix typos and html styling.)
# Create your views here.

def studentView(request):
	return render(request, "student/studentView.html", {})

def rateClass(request):
	if request.method == "POST":
		form = RateClassForm(request.POST)

		if form.is_valid():
			form.save()
	else:
		form = RateClassForm()
	return render(request, "student/rateClass.html", {"form":form})

def fileComplaint(request):
	if request.method == "POST":
		form = FileComplaintForm(request.POST)

		if form.is_valid():
			form.save()
	else:
		form = FileComplaintForm()
	return render(request, "student/fileComplaint.html", {"form":form})
<<<<<<< Updated upstream
=======

<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> parent of e150cc2 (Merge pull request #7 from yqian000/addUser)
=======
>>>>>>> parent of e2cf0a5 (Fix typos and html styling.)


def Application(request):
	if request.method=="POST":
		form=ApplicationForm(request.POST, request.FILES)
			
		application=Application(email=request.POST['email'],firstname=request.POST['firstname'],lastname=request.POST['lastname'],Gpa=request.POST['Gpa'],semester=request.POST['semester'],Birthday=request.POST['Birthday'],address=request.POST['address'],city=request.POST['city'],state=request.POST['state'],zip=request.POST['zip'],country=request.POST['country'],letters=request.FILES["letters"],personal_statement=request.FILES['personal_statement'],major=request.POST['Major'],transcprit=request.FILES['transcprit'])
		application.save()
		return redirect("home")
	else:
			form=applicationForm()

	context={'form':form}
	return render(request,'main/admission.html',context)
	
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> Stashed changes
>>>>>>> parent of e2cf0a5 (Fix typos and html styling.)
=======
>>>>>>> Stashed changes
>>>>>>> parent of e150cc2 (Merge pull request #7 from yqian000/addUser)
=======
>>>>>>> Stashed changes
>>>>>>> parent of e2cf0a5 (Fix typos and html styling.)
