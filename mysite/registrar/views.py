from django.shortcuts import render

# Create your views here.
def registrarView(request):
	return render(request, "registrar/registrarView.html", {})

def viewNewUser(request):
	return render(request, "registrar/viewNewUser.html", {})

def viewGrad(request):
	return render(request, "registrar/viewGrad.html", {})

def viewRating(request):
	return render(request, "registrar/viewRating.html", {})

def setClass(request):
	return render(request, "registrar/setClass.html", {})

def manageComplaint(request):
	return render(request, "registrar/manageComplaint.html", {})

def manageSuspension(request):
	return render(request, "registrar/manageSuspension.html", {})
