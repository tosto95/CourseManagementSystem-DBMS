from __future__ import unicode_literals

from django.db import models
from CourseList.models import CourseList, StudentRegistration
# Create your models here.


class Assignment(models.Model):
	assignmentID = models.AutoField(primary_key = True)
	courseID = models.ForeignKey(CourseList,  on_delete = models.CASCADE, null = True)
	studentID = models.ForeignKey(StudentRegistration, on_delete = models.CASCADE, null = True)
	assignMarks1 = models.IntegerField('Assignment1 Marks', default = 0)
	assignMarks2 = models.IntegerField('Assignment2 Marks', default = 0)
	assignMarks3 = models.IntegerField('Assignment3 Marks', default = 0)
	assignMarks4 = models.IntegerField('Assignment4 Marks', default = 0)
	assignMarks5 = models.IntegerField('Assignment5 Marks', default = 0)
	assignMarks6 = models.IntegerField('Assignment6 Marks', default = 0)
	assignMarks7 = models.IntegerField('Assignment7 Marks', default = 0)
	assignMarks8 = models.IntegerField('Assignment8 Marks', default = 0)

class Content(models.Model):
	ContentID = models.AutoField(primary_key = True)
	courseID = models.ForeignKey(CourseList,   on_delete = models.CASCADE)
	Lecture1 = models.CharField('Lecture1', max_length = 100, null = True)
	Lecture2 = models.CharField('Lecture2', max_length = 100, null = True)
	Lecture3 = models.CharField('Lecture3', max_length = 100, null = True)
	Lecture4 = models.CharField('Lecture4', max_length = 100, null = True)
	Lecture5 = models.CharField('Lecture5',max_length = 100, null = True)
	Lecture6 = models.CharField('Lecture6', max_length = 100, null = True)
	Lecture7 = models.CharField('Lecture7', max_length = 100, null = True)
	Lecture8 = models.CharField('Lecture8', max_length = 100, null = True)
	Assignment1 = models.CharField('Assignment1', max_length = 100, null = True)
	Assignment2 = models.CharField('Assignment2', max_length = 100, null = True)
	Assignment3 = models.CharField('Assignment3', max_length = 100, null = True)
	Assignment4 = models.CharField('Assignment4', max_length = 100, null = True)
	Assignment5 = models.CharField('Assignment5', max_length = 100, null = True)
	Assignment6 = models.CharField('Assignment6', max_length = 100, null = True)
	Assignment7 = models.CharField('Assignment7', max_length = 100, null = True)
	Assignment8 = models.CharField('Assignment8', max_length = 100, null = True)
	Test1 = models.CharField('Test1', max_length = 100, null = True)
	Test2 = models.CharField('Test2', max_length = 100, null = True)
	Test3 = models.CharField('Test3', max_length = 100, null = True)
	Test4 = models.CharField('Test4', max_length = 100, null = True)

	

class Test(models.Model):
	assignmentID = models.AutoField(primary_key = True)
	courseID = models.ForeignKey(CourseList,   on_delete = models.CASCADE, null = True)
	studentID = models.ForeignKey(StudentRegistration, on_delete = models.CASCADE, null = True)
	testMarks1 = models.IntegerField('Test1 Marks', default = 0)
	testMarks2 = models.IntegerField('Test2 Marks', default = 0)
	testMarks3 = models.IntegerField('Test3 Marks', default = 0)
	testMarks4 = models.IntegerField('Test4 Marks', default = 0)
