from __future__ import unicode_literals

from django.db import models
from CourseList.models import CourseList
from People.models import Student
# Create your models here.

class Content(models.Model):
	week = models.AutoField(primary_key = True)
	courseID = models.ForeignKey(CourseList, on_delete = models.CASCADE)
	lectures = models.CharField(max_length = 10000)
	assignment = models.CharField(max_length = 10000)
	tests = models.CharField(max_length = 10000)
	
class Assignment(models.Model):
	week = models.AutoField(primary_key = True)
	studentID = models.ForeignKey(Student, on_delete = models.CASCADE)
	assignMarks1 = models.IntegerField()
	assignMarks2 = models.IntegerField()
	assignMarks3 = models.IntegerField()
	assignMarks4 = models.IntegerField()
	assignMarks5 = models.IntegerField()
	assignMarks6 = models.IntegerField()
	assignMarks7 = models.IntegerField()
	assignMarks8 = models.IntegerField()

class Test(models.Model):
	week = models.AutoField(primary_key = True)
	studentID = models.ForeignKey(Student, on_delete = models.CASCADE)
	testMarks1 = models.IntegerField()
	testMarks2 = models.IntegerField()
	testMarks3 = models.IntegerField()
	