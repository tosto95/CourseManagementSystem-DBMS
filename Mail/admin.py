from django.contrib import admin

# Register your models here.
from .models import Student_Faculty_Mail, Faculty_Student_Mail

admin.site.register(Student_Faculty_Mail)
admin.site.register(Faculty_Student_Mail)