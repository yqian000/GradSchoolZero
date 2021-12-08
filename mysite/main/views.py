from django.shortcuts import render
from account.models import *

# Create your views here.
def home(request):
	students = Student.objects.all()
	courses = Course.objects.all()
	max_rate = 0
	min_rate = 5
	max_gpa = 0

	for student in students:
		if student.GPA > max_gpa:
			max_gpa = student.GPA
	top_students = Student.objects.filter(GPA=max_gpa)

	for course in courses:
		if course.rate is not None and course.rate > max_rate:
			max_rate = course.rate
	top_classes = Course.objects.filter(rate=max_rate)

	for course in courses:
		if course.rate is not None and course.rate < min_rate:
			min_rate = course.rate
	low_classes = Course.objects.filter(rate=min_rate)

	return render(request, "main/home.html", {'ts': top_students, 'tc': top_classes, 'lc': low_classes, 'c':courses})


