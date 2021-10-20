from django.shortcuts import render
from .forms import RateClassForm, FileComplaintForm
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
