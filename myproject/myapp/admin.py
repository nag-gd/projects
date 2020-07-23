from django.contrib import admin
from .models import Friends

# Register your models here.

class FriendsAdmin(admin.ModelAdmin):
    list_display=['name','profession','organization','working_city','phone', ]

admin.site.register(Friends, FriendsAdmin)