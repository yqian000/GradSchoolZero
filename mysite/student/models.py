from django.db import models

<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< Updated upstream
# Create your models here.
=======
>>>>>>> parent of e150cc2 (Merge pull request #7 from yqian000/addUser)
=======
<<<<<<< Updated upstream
# Create your models here.
=======
>>>>>>> parent of e2cf0a5 (Fix typos and html styling.)
class Applcation(models.Model):
    email=models.EmailField()
    firstname=models.CharField(max_length=150,blank="True")
    lastname=models.CharField(max_length=150,blank="True")
    Gpa=models.CharField(max_length=150,blank="True")
    semester=models.CharField(max_length=150,blank="True")
    Birthday=models.DateField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60, default="NewYork")
    state = models.CharField(max_length=30, default="NewYork")
    zip = models.CharField(max_length=5, default="11220")
    country = models.CharField(max_length=50)
    transcprit= models.FileField(upload_to='student/documents/')
    letters= models.FileField(upload_to='student/documents/')
    personal_statement = models.FileField(upload_to='student/documents/')
    major=models.CharField(max_length=150,blank="True")
 


<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> Stashed changes
>>>>>>> parent of e150cc2 (Merge pull request #7 from yqian000/addUser)
=======
>>>>>>> Stashed changes
>>>>>>> parent of e2cf0a5 (Fix typos and html styling.)
