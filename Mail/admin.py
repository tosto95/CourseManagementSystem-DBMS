from django.contrib import admin

# Register your models here.
from .models import StudentFacultyMail, FacultyStudentMail

admin.site.register(StudentFacultyMail)
admin.site.register(FacultyStudentMail)