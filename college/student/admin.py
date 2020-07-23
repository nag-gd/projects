from django.contrib import admin
from student.models import Student


# call models here

class StudentAdmin(admin.ModelAdmin):
    list_display=['name', 'roll']



# Register your models here.

admin.site.register(Student, StudentAdmin)