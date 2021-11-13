from django.urls import path

from . import views

urlpatterns = [
	path('instructorView/', views.instructorView, name='instructorView'),
	path('accessCourse/', views.accessCourse, name='accessCourse'),
	path('assignGrade/', views.assignGrade, name='assignGrade'),
	path('complaintStudent/', views.complaintStudent, name='complaintStudent'),
	path('viewWaitlist/', views.viewWaitlist, name='viewWaitlist'),
]