from django.urls import path

from . import views

urlpatterns = [
	path('instructorView/', views.instructorView, name='instructorView'),
	path('accessCourse/', views.accessCourse, name='accessCourse'),
	path('assignGrade/', views.assignGrade, name='assignGrade'),
	path('grade/<int:pk>',views.grade,name='grade'),
	path('complaintStudent/', views.complaintStudent, name='complaintStudent'),
	path('viewWaitlist/', views.viewWaitlist, name='viewWaitlist'),
	path('career/', views.JobApplication, name='career'),
	path('acceptlist/<int:pk>',views.accept_waiting_list,name='acceptlist'),
	path('rejectlist/<int:pk>',views.reject_waiting_list,name="rejectlist"),
	path('accessCourse/',views.accessCourse,name="accessCourse")


]