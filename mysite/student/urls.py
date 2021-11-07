from django.urls import path

from . import views

urlpatterns = [
	path('studentView/', views.studentView, name='studentView'),
	path('rateClass/', views.rateClass, name='rateClass'),
<<<<<<< HEAD
	path('fileComplaint/', views.fileComplaint, name='fileComplaint'),]
=======
<<<<<<< Updated upstream
	path('fileComplaint/', views.fileComplaint, name='fileComplaint'),
=======
	path('admission/', views.Application, name='admission'),
	

>>>>>>> Stashed changes
]
>>>>>>> parent of e2cf0a5 (Fix typos and html styling.)
