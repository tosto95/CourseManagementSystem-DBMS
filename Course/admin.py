from django.contrib import admin

# Register your models here.
from .models import Assignment, Content, Test

admin.site.register(Assignment)
admin.site.register(Content)
admin.site.register(Test)