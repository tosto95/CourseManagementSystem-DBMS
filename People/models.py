from __future__ import unicode_literals
import datetime
from django.utils import timezone
from django.db import models

# Create your models here

class Student(models.Model):
	studentID = models.AutoField(primary_key = True)
	firstName = models.CharField('First Name',max_length = 100)
	lastName = models.CharField('Last Name',max_length = 100)
	dob = models.DateField('Date of Birth')
	age = models.IntegerField()
	studentUserName = models.CharField('Login Username',max_length = 100)
	studentPassword = models.CharField('Login Password',max_length = 100)
	def __str__(self):
		return self.studentID

class Faculty(models.Model):
	facultyID = models.AutoField(primary_key = True)
	firstName = models.CharField('First Name',max_length = 100)
	lastName = models.CharField('Last Name',max_length = 100)
	dob = models.DateField('Date of Birth')
	age = models.IntegerField()
	facultyUserName = models.CharField('Login Username',max_length = 100)
	facultyPassword = models.CharField('Login Password',max_length = 100)
	def __str__(self):
		return self.facultyID

class Parent(models.Model):
	parentID = models.AutoField(primary_key = True)
	firstName = models.CharField('First Name',max_length = 100)
	lastName = models.CharField('Last Name',max_length = 100)
	parentUserName = models.CharField('Login Username',max_length = 100)
	parentPassword = models.CharField('Login Password',max_length = 100)
	def __str__(self):
		return self.parentID

class Admin(models.Model):
	adminID = models.AutoField(primary_key = True)
	firstName = models.CharField('First Name',max_length = 100)
	lastName = models.CharField('Last Name',max_length = 100)
	adminUserName = models.CharField('Login Username',max_length = 100)
	adminPassword = models.CharField('Login Password',max_length = 100)
	def __str__(self):
		return self.adminID


class Student_Parent(models.Model):
	studentID = models.ForeignKey(Student, on_delete = models.CASCADE)
	parentID = models.ForeignKey(Parent, on_delete = models.CASCADE)



