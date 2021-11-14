from django.shortcuts import render
from account.models import *

# Create your views here.
def home(request):
	return render(request, "main/home.html", {})


