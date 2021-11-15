from django.urls import path
import tkinter
from tkinter import messagebox

from . import views

urlpatterns = [
	path('registrarView/', views.registrarView, name='registrarView'),
	path('viewNewUser/', views.viewNewUser, name='viewNewUser'),
	path('viewGrad/', views.viewGrad, name='viewGrad'),
	path('viewRating/', views.viewRating, name='viewRating'),
	path('setClass/', views.setClass, name='setClass'),
	path('manageComplaint/', views.manageComplaint, name='manageComplaint'),
	path('processStudentComplaint/<int:pk>', views.processStudentComplaint, name='processStudentComplaint'),
	path('processInstructorComplaint/<int:pk>', views.processInstructorComplaint, name='processInstructorComplaint'),
	path('manageSuspension/', views.manageSuspension, name='manageSuspension'),
	path('rejectapplications/<int:pk>', views.rejectapplications, name='rejectapplications'),
	path('acceptapplications/<int:pk>', views.acceptapplications, name='acceptapplications'),
]