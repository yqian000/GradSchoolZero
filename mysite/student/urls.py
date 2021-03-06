from django.urls import path

from . import views

urlpatterns = [
    path('studentView/', views.studentView, name='studentView'),
    path('rateClass/', views.rateClass, name='rateClass'),
    path('dropClass/', views.dropClass, name='dropClass'),
    path('processDropClass/<int:pk>', views.processDropClass, name='processDropClass'),
    path('fileComplaint/', views.fileComplaint, name='fileComplaint'),
    path('applyGrad/', views.applyGrad, name='applyGrad'),
    path('admission/', views.Application, name='admission'),
    path('tutorial/', views.tutorial, name='tutorial'),
    path('enrollment/', views.avalibleclasses, name='enrollment'),
    path('addclass/<int:pk>', views.add_sucessfully, name='addclass'),
    path('enrollmentcart/', views.enrollmentcart, name='enrollmentcart'),
    path('deletenrollemt/<int:pk>', views.deletefromEnrollment, name='deletenrollemt'),
    path('enrollpage/', views.enroll, name='enrollpage'),
    path('deleteAll/', views.clearall, name='deleteAll'),

]
