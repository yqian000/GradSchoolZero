from django.urls import path

from . import views

urlpatterns = [
	path('studentView/', views.studentView, name='studentView'),
	path('rateClass/', views.rateClass, name='rateClass'),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	path('fileComplaint/', views.fileComplaint, name='fileComplaint'),]
=======
=======
>>>>>>> parent of e150cc2 (Merge pull request #7 from yqian000/addUser)
=======
>>>>>>> parent of e2cf0a5 (Fix typos and html styling.)
<<<<<<< Updated upstream
	path('fileComplaint/', views.fileComplaint, name='fileComplaint'),
=======
	path('admission/', views.Application, name='admission'),
	

>>>>>>> Stashed changes
<<<<<<< HEAD
<<<<<<< HEAD
]
>>>>>>> parent of e2cf0a5 (Fix typos and html styling.)
=======
]
>>>>>>> parent of e150cc2 (Merge pull request #7 from yqian000/addUser)
=======
]
>>>>>>> parent of e2cf0a5 (Fix typos and html styling.)
