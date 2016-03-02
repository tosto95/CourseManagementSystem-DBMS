from __future__ import unicode_literals

from django.db import models
from People.models import Student, Faculty
import datetime
from django.utils import timezone

# Create your models here.

class CourseList(models.Model):
	courseID=models.AutoField(primary_key = True)
	courseName=models.CharField('Course Name' , max_length=100)
	startDate=models.DateTimeField('Start Date')
	endDate=models.DateTimeField('End Date')
	faculty =models.ForeignKey(Faculty, on_delete=models.SET_NULL, null = True)
	def __str__(self):
		return str(self.courseID)

class StudentRegistration(models.Model):
	studentID=models.ForeignKey(Student, on_delete=models.SET_NULL, null = True)
	courseID=models.ForeignKey(CourseList, on_delete=models.CASCADE, null = True)
	grade = models.CharField('Grade',max_length = 100, null = True)
	progress = models.CharField('Progress',max_length = 100, null = True)
	def __str__(self):
		return str(self.studentID)
	
