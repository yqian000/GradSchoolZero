from django.shortcuts import render,redirect
from .forms import *
from .models import *
from registrar.models import Taboo
from account.models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from registrar.models import *
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
		s = Student.objects.get(email=request.user.email)

		# validate if the student is currently enrolled in the course
		# code goes here
		
		c = RateClass(email=s.email)
		tabooList = Taboo.objects.all()
		warning = 0

		# clean up reviews and update warning if any
		post = request.POST.copy()
		review = (post['review']).lower()
		for taboo in tabooList:
			word = (taboo.word).lower()
			while word in review:
				review = review.replace(word, '*', 1)
				warning = warning + 1

		# update warning
		if warning > 2:
			s.warning += 2
			s.save()
			form = RateClassForm()
			return render(request, "student/rateClass.html", {"form":form})
		elif warning > 0:
			s.warning += 1
			s.save()

		# update POST and save to db
		post['review'] = review
		request.POST = post
		form = RateClassForm(request.POST, instance=c)

		if form.is_valid():
			form.save()

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
	student=Student.objects.get(email=request.user)
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
		if Period.objects.last().is_course_registration or Student.objects.get(email=request.user).is_special_assigned:
		
				
					st=Student.objects.get(email=request.user)#student
					CD=Cart.objects.filter(Email=request.user)#course has been added to cart
					row=[]
					for ID in range(len(CD)):
							if CD[ID].CourseID not in row:
								row.append(CD[ID].CourseID)
					
					# course in enrollment cart
					course=[Course.objects.get(id=x) for x in row]
					
					if len(Cart.objects.filter(Email=request.user))+len(course_record.objects.filter(student_email=request.user,grade=""))>4:
						messages.success(request, "Enroll failed, you have reached the maxmium classes you can take per semester") # this ends *after* next_ starts
						return redirect("enrollmentcart")
					for	i in range(len(CD)):
							# to check if the courses in enrollemnt cart is already in the enrolled classes 
						if  len(course_record.objects.filter(student_email=request.user,course_name=course[i].name,grade=""))>0:
							messages.success(request, "Enroll failed, you tried to enroll same classes")
							return redirect("enrollmentcart")

						try:
							if  course_record.objects.filter(student_email=request.user,course_name=course[i].name).reverse()[0]!="F":
									messages.success(request, "Enroll Failed,according to CUNY policy, students can't retake the courses if they got D or higer before")
									return redirect("enrollmentcart")
						except:
							pass
				
					

					cd=[Cart.objects.get(id=CD[ID].id) for ID in range(len(CD))]

					
					
					Monday=[]
					Tuseday=[]
					Wednesday=[]
					Thurseday=[]
					Friday=[]
					
					for i in range (len(course)):
						if  "Monday".lower() in course[i].meeting_date.lower():
							Monday.append([float(course[i].start_time),float(course[i].end_time)])
							Monday.sort()
						if  "Tuseday".lower() in course[i].meeting_date.lower():
							Tuseday.append([float(course[i].start_time),float(course[i].end_time)])
							Tuseday.sort()
						if "Wednesday".lower() in course[i].meeting_date.lower():
							Wednesday.append([float(course[i].start_time),float(course[i].end_time)])
							Wednesday.sort()
						if "Thurseday".lower() in course[i].meeting_date.lower():
							Thurseday.append([float(course[i].start_time),float(course[i].end_time)])
							Thurseday.sort()
						if "Friday".lower() in course[i].meeting_date.lower():
							Friday.append([float(course[i].start_time),float(course[i].end_time)])
							Friday.sort()
					
					try:
						# course has enrolled
						C=st.course.all()
						for i in range (len(C)):
							if  "Monday".lower() in C[i].meeting_date.lower():
								Monday.append([float(C[i].start_time),float(C[i].end_time)])
								Monday.sort()
							if  "Tuseday".lower() in C[i].meeting_date.lower():
								Tuseday.append([float(C[i].start_time),float(C[i].end_time)])
								Tuseday.sort()
							if "Wednesday".lower() in C[i].meeting_date.lower():
								Wednesday.append([float(C[i].start_time),float(C[i].end_time)])
								Wednesday.sort()
							if "Thurseday".lower() in C[i].meeting_date.lower():
								Thurseday.append([float(C[i].start_time),float(C[i].end_time)])
								Thurseday.sort()
							if "Friday".lower() in C[i].meeting_date.lower():
								Friday.append([float(C[i].start_time),float(C[i].end_time)])
								Friday.sort()
					except:
						pass
						
					for i, this in enumerate(Monday):
							for next_ in Monday[i+1:]:
								if this[1] > next_[0]: 
									messages.success(request, 'Schedule conflicts founded, enroll failed') # this ends *after* next_ starts
									return redirect("enrollmentcart")
								
					for i, this in enumerate(Tuseday):
							for next_ in Thurseday[i+1:]:
								if this[1] > next_[0]:  # this ends *after* next_ starts
									return redirect("enrollmentcart")
					for i, this in enumerate(Thurseday):
							for next_ in Thurseday[i+1:]:
								if this[1] > next_[0]:  # this ends *after* next_ starts
									return redirect("enrollmentcart")
					for i, this in enumerate(Wednesday):
							for next_ in Wednesday[i+1:]:
								if this[1] > next_[0]:  # this ends *after* next_ starts
									return redirect("enrollmentcart")
					for i, this in enumerate(Friday):
							for next_ in Friday[i+1:]:
								if this[1] > next_[0]:  # this ends *after* next_ starts
									return redirect("enrollmentcart")
					
					
					
					for i in course :
						if i. curr_size>=i.max_size:
							
							try:
								CR=course_record(course_name=i.name,Instructor_email=i.instructor,student_email=st.email,waiting_list=True)
								CR.save()
								st.cr=CR
								st.save()
							except:
								CR=course_record(course_name=i.name,Instructor_email="TBD",student_email=st.email,waiting_list=True)
								CR.save()
								st.cr=CR
								st.save()
							messages.success(request,i.name+"has been put in waiting list")
							if(len(course))==1:
								return redirect("enrollmentcart")

						else:
							
							try:
								CR=course_record(course_name=i.name,Instructor_email=i.instructor,student_email=st.email)
								CR.save()
							except:
								CR=course_record(course_name=i.name,Instructor_email="TBD",student_email=st.email)
								CR.save()
							st.cr=CR
							st.save()
							st.course.add(i)
							i.curr_size+=1
							i.save()
							st.save()
						
					for c in cd:
						c.delete()
					messages.success(request, "You've sucessfully enrolled in the classes")
					return redirect("enrollmentcart")
	except:	
				messages.success(request, "oops!Something went wrong..")
				return redirect("enrollmentcart")
	else:
			messages.success(request, "Currently not allowd to enroll any  classes ")
			return redirect("enrollmentcart")
def clearall(request):
		try:
			CD=Cart.objects.filter(Email=request.user)
			for  i in CD:
				i.delete()
			messages.success(request, 'Your cart has been cleared')
			return redirect("enrollmentcart")
		except:
			print("Hello")
			messages.success(request, 'Somthing seems wrong, please try it one more time')
			return redirect("enrollmentcart")