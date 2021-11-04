from django.urls import path

from . import views

urlpatterns = [
	path('studentView/', views.studentView, name='studentView'),
	path('rateClass/', views.rateClass, name='rateClass'),
<<<<<<< Updated upstream
	path('fileComplaint/', views.fileComplaint, name='fileComplaint'),
=======
	path('admission/', views.Application, name='admission'),
	

>>>>>>> Stashed changes
]