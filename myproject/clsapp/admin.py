from django.contrib import admin
from .models import Book, Company

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=['title', 'author', 'price']

admin.site.register(Book,BookAdmin)

class CompanyAdmin(admin.ModelAdmin):
    List_Display=['name', 'location', 'ceo']

admin.site.register(Company, CompanyAdmin)