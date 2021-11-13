from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=60)

	def __str__(self):
		return self.name

		