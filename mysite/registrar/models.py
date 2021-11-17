from django.db import models

# Create your models here.
class Taboo(models.Model):
    word=models.CharField(max_length=100, unique=True)