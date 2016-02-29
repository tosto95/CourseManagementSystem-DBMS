from __future__ import unicode_literals

from django.db import models

# Create your models here

class Student(models.Model):
	studentID = models.AutoField(primary_key = True)
	firstName = models.CharField(max_length = 100)
	lastName = models.CharField(max_length = 100)
	dob = models.DateTimeField('Date of Birth')
	age = models.IntegerField()
	studentUserName = models.CharField(max_length = 100)
	studentPassword = models.CharField(max_length = 100)
	def __str__(self):
		return self.studentID

class Faculty(models.Model):
	facultyID = models.AutoField(primary_key = True)
	firstName = models.CharField(max_length = 100)
	lastName = models.CharField(max_length = 100)
	dob = models.DateTimeField('Date of Birth')
	age = models.IntegerField()
	facultyUserName = models.CharField(max_length = 100)
	facultyPassword = models.CharField(max_length = 100)
	def __str__(self):
		return self.facultyID

class Parent(models.Model):
	parentID = models.AutoField(primary_key = True)
	firstName = models.CharField(max_length = 100)
	lastName = models.CharField(max_length = 100)
	parentUserName = models.CharField(max_length = 100)
	parentPassword = models.CharField(max_length = 100)
	def __str__(self):
		return self.parentID

class Admin(models.Model):
	adminID = models.AutoField(primary_key = True)
	firstName = models.CharField(max_length = 100)
	lastName = models.CharField(max_length = 100)
	adminUserName = models.CharField(max_length = 100)
	adminPassword = models.CharField(max_length = 100)
	def __str__(self):
		return self.adminID


class Student_Parent(models.Model):
	studentID = models.ForeignKey(Student, on_delete = models.CASCADE)
	parentID = models.ForeignKey(Parent, on_delete = models.CASCADE)



	