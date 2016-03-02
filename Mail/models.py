from __future__ import unicode_literals

from django.db import models
from People.models import Student, Faculty

# Create your models here.
class StudentFacultyMail(models.Model):
	studentID = models.ForeignKey(Student, on_delete=models.SET_NULL, null = True)
	message = models.CharField(max_length = 1000)
	facultyID = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null = True)
	def __str__(self):
		return self.message
	

class FacultyStudentMail(models.Model):	
	facultyID = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null = True)
	message = models.CharField(max_length = 1000)
	studentID = models.ForeignKey(Student, on_delete=models.SET_NULL, null = True)
	def __str__(self):
		return self.message
