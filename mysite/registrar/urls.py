from django.urls import path

from . import views

urlpatterns = [
	path('registrarView/', views.registrarView, name='registrarView'),
	path('viewNewUser/', views.viewNewUser, name='viewNewUser'),
	path('viewGrad/', views.viewGrad, name='viewGrad'),
	path('viewRating/', views.viewRating, name='viewRating'),
	path('setClass/', views.setClass, name='setClass'),
	path('manageComplaint/', views.manageComplaint, name='manageComplaint'),
	path('manageSuspension/', views.manageSuspension, name='manageSuspension'),
]