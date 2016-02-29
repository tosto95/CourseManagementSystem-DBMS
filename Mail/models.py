from __future__ import unicode_literals

from django.db import models
from People.models import Student, Faculty

# Create your models here.
class Student_Faculty_Mail(models.Model):
	studentID = models.ForeignKey(Student, on_delete=models.SET_NULL, null = True)
	message = models.CharField(max_length = 1000)
	facultyID = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null = True)
	

class Faculty_Student_Mail(models.Model):	
	facultyID = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null = True)
	message = models.CharField(max_length = 1000)
	studentID = models.ForeignKey(Student, on_delete=models.SET_NULL, null = True)

