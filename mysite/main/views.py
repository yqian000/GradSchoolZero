from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
	student = Student.objects.get(id=1)
	return render(request, "main/home.html", {"student": student})

def signup(request):
	return render(request, "main/signup.html", {})

def login(request):
	return render(request, "main/login.html", {})
