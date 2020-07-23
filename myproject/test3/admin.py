from django.contrib import admin
from .models import Teacher,Student,Post


class PostAdmin(admin.ModelAdmin):
    list_display=['title', 'slug', 'author', 'body', 'publish', 'created', 'modified', 'status']
    prepopulated_fields={'slug':('title',)}
    list_filter=('status','author')
    raw_id_fields=('author',)


# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Post,PostAdmin)