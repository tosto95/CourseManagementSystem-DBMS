from __future__ import unicode_literals

from django.db import models
from People.models import Student, Faculty
import datetime
from django.utils import timezone

# Create your models here.

class CourseList(models.Model):
	courseID=models.AutoField(primary_key = True)
	courseName=models.CharField(max_length=100)
	startDate=models.DateTimeField('Start Date')
	endDate=models.DateTimeField('End Date')
	faculty1=models.ForeignKey(Faculty, on_delete=models.SET_NULL, null = True, related_name="%(app_label)s_%(class)s_related")
	faculty2=models.ForeignKey(Faculty, on_delete=models.SET_NULL, null = True)

class StudentRegistration(models.Model):
	studentID=models.ForeignKey(Student, on_delete=models.SET_NULL, null = True)
	courseID=models.ForeignKey(CourseList, on_delete=models.SET_NULL, null = True)

		
