from django.contrib import admin

# Register your models here.
from .models import Content, Assignment, Test

admin.site.register(Content)
admin.site.register(Assignment)
admin.site.register(Test)

