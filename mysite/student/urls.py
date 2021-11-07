from django.urls import path

from . import views

urlpatterns = [
	path('studentView/', views.studentView, name='studentView'),
	path('rateClass/', views.rateClass, name='rateClass'),
	path('fileComplaint/', views.fileComplaint, name='fileComplaint'),
<<<<<<< HEAD
	path('admission/', views.Application, name='admission'),
	
=======
>>>>>>> parent of d70f5b3 (prototype of admission table database and form)
]