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
	path('processClass/<int:pk>', views.processClass, name='processClass'),
	path('manageComplaint/', views.manageComplaint, name='manageComplaint'),
	path('processStudentComplaint/<int:pk>', views.processStudentComplaint, name='processStudentComplaint'),
	path('processInstructorComplaint/<int:pk>', views.processInstructorComplaint, name='processInstructorComplaint'),
	path('manageSuspension/', views.manageSuspension, name='manageSuspension'),
	path('processSuspension/<int:pk>', views.processSuspension, name='processSuspension'),
	path('rejectapplications/<int:pk>', views.rejectapplications, name='rejectapplications'),
	path('acceptapplications/<int:pk>', views.acceptapplications, name='acceptapplications'),
	path('tabooList/', views.tabooList, name='tabooList'),
	path('rejectjobapplications/<int:pk>', views.reject_job_application, name='rejectjobapplications'),
	path('acceptjobapplications/<int:pk>', views.accept_job_applications, name='acceptjobapplications'),
	path('periodsetup/', views.PeriodSetup, name='periodsetup'),
	path('setClass/', views.setClass, name='setClass'),
	path('honorlist/', views.honor, name='honorlist'),
	path('assignhonor/', views.assignhonor, name='assignhonor'),
	path('suspeciousactivity/', views.suspecious, name='suspeciousactivity'),
	path('sendnotification<int:pk>/', views.sendemail, name='sendnotification'),
	path('Fire<int:pk>/', views.Fire, name='fire'),
	path('ignore<int:pk>/', views.ignore, name='ignore'),
]