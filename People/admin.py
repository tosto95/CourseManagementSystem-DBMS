from django.contrib import admin

# Register your models here.

from .models import Student, Parent, Faculty, Admin, StudentParent

admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Parent)
admin.site.register(Admin)
admin.site.register(StudentParent)

