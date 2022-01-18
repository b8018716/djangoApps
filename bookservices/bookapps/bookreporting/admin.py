from django.contrib import admin
from .models import Book
@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display=['name','submitter']


# Register your models here.
