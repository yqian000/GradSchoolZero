from django.shortcuts import render
from account.models import *

# Create your views here.
def home(request):
	student = Student.objects.get(user=request.user)
	return render(request, "main/home.html", {'user': request.user,'s': student})


