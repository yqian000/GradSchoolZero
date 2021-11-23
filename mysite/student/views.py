from django.shortcuts import render,redirect
from .forms import *
from .models import *
from account.models import *
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def studentView(request):


	try:
		if request.user.is_student:
			student = Student.objects.get(user=request.user)
			if student.warning == 3:
				student.fine = 1 # set to has fine
				student.is_suspended = True
				student.save()

			return render(request, "student/studentView.html", {"s":student})
		else:
			return render(request, "main/forbidden.html",{})
	except:
			return render(request, "main/forbidden.html",{})
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
		# create a new StudentComplaint model and set the ID and is_completed
		c = StudentComplaint(user_id=Student.objects.get(email=request.user.email).ID, is_completed=False)
		form = FileComplaintForm(request.POST, instance=c)

		if form.is_valid():
			form.save()
	
	form = FileComplaintForm()
	return render(request, "student/fileComplaint.html", {"form":form, "r":request})

def Application(request):
	if request.method=="POST":
		form=applicationForm(request.POST, request.FILES)
			
		application=Applcation(email=request.POST['email'],firstname=request.POST['firstname'],lastname=request.POST['lastname'],Gpa=request.POST['Gpa'],semester=request.POST['semester'],Birthday=request.POST['Birthday'],address=request.POST['address'],city=request.POST['city'],state=request.POST['state'],zip=request.POST['zip'],country=request.POST['country'],letters=request.FILES["letters"],personal_statement=request.FILES['personal_statement'],major=request.POST['Major'],transcprit=request.FILES['transcprit'])
		application.save()
		return redirect("home")
	else:
		form=applicationForm()

	context={'form':form}
	return render(request,'main/admission.html',context)
	
def tutorial(request):
	return render(request, "student/tutorial.html", {})
def avalibleclasses(request):
	courses=Course.objects.filter(is_open=True)
	return render(request,'student/Enrollment.html',{"courses":courses})
def add_sucessfully(request,pk):
	student=Student.objects.filter(email=request.user)[0]
	Enroll=Cart(CourseID=pk,Email=student.email)
	Enroll.save()
	student.enrollcart=Enroll
	student.save()
	courses=Course.objects.filter(is_open=True)
	return redirect("enrollment")
def enrollmentcart(request):
	
	try:
		CD=Cart.objects.filter(Email=request.user)
		row=[]
		for ID in range(len(CD)):
				if CD[ID].CourseID not in row:
					row.append(CD[ID].CourseID)
		course=[Course.objects.get(id=x) for x in row]

		cd=[Cart.objects.get(id=CD[ID].id) for ID in range(len(CD))]
		return render(request,'student/Enrollmentcart.html',{'all_data': zip(course, cd)})
	except:
		return render(request,'student/Enrollmentcart.html',{'all_data': zip(course, cd)})

def deletefromEnrollment(request,pk=None):

	try:
		if Cart.objects.get(id=pk)!=None:
	
				Cart.objects.get(id=pk).delete()
			

		return redirect("enrollmentcart")

	except:
			
		return redirect("enrollmentcart")

def enroll(request):
	try:
		st=Student.objects.get(email=request.user)
		CD=Cart.objects.filter(Email=request.user)
		row=[]
		for ID in range(len(CD)):
				if CD[ID].CourseID not in row:
					row.append(CD[ID].CourseID)
		

		cd=[Cart.objects.get(id=CD[ID].id) for ID in range(len(CD))]

		course=[Course.objects.get(id=x) for x in row]
		
		Monday=[]
		Tuseday=[]
		Wednesday=[]
		Thurseday=[]
		Friday=[]

		for i in range (len(course)):
				
			if course[i].meeting_date.lower()=="Monday".lower():
				Monday.append([float(course[i].start_time),float(course[i].end_time)])
				Monday.sort()
			if course[i].meeting_date.lower()=="Tuseday".lower():
				Tuseday.append([float(course[i].start_time),float(course[i].end_time)])
				Tuseday.sort()
			if course[i].meeting_date.lower()=="Wednesday".lower():
				Wednesday.append([float(course[i].start_time),float(course[i].end_time)])
				Wednesday.sort()
			if course[i].meeting_date.lower()=="Thurseday".lower():
				Thurseday.append([float(course[i].start_time),float(course[i].end_time)])
				Thurseday.sort()
			if course[i].meeting_date.lower()=="Friday".lower():
				Friday.append([float(course[i].start_time),float(course[i].end_time)])
				Friday.sort()
		conflicts = []
		message =None
		for i, this in enumerate(Monday):
				for next_ in Monday[i+1:]:
					if this[1] > next_[0]:  # this ends *after* next_ starts
						message="Schedule conflicts! Enrollment failed"
						return render(request,'student/Enrollmentcart.html',{'all_data': zip(course, cd),'m':message})
					
		for i, this in enumerate(Tuseday):
				for next_ in Thurseday[i+1:]:
					if this[1] > next_[0]:  # this ends *after* next_ starts
						message="Schedule conflicts! Enrollment failed"
						return render(request,'student/Enrollmentcart.html',{'all_data': zip(course, cd),'m':message})
		for i, this in enumerate(Thurseday):
				for next_ in Thurseday[i+1:]:
					if this[1] > next_[0]:  # this ends *after* next_ starts
						message="Schedule conflicts! Enrollment failed"
						return render(request,'student/Enrollmentcart.html',{'all_data': zip(course, cd),'m':message})
		for i, this in enumerate(Wednesday):
				for next_ in Wednesday[i+1:]:
					if this[1] > next_[0]:  # this ends *after* next_ starts
						message="Schedule conflicts! Enrollment failed"
						return render(request,'student/Enrollmentcart.html',{'all_data': zip(course, cd),'m':message})
		for i, this in enumerate(Friday):
				for next_ in Friday[i+1:]:
					if this[1] > next_[0]:  # this ends *after* next_ starts
						message="Schedule conflicts! Enrollment failed Check it carefully"
						return render(request,'student/Enrollmentcart.html',{'all_data': zip(course, cd),'m':message})
		

		
		for i in course :
			i.student.add(st)
			i.curr_size+=1
			i.max_size-=1
			i.save()
		for c in cd:
			c.delete()
		return redirect("enrollmentcart",m=message)
	except:


		return render(request,'student/Enrollmentcart.html',{'all_data': zip(course, cd),'m':message})