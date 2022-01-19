from django.contrib import admin
from .models import Book, Author
@admin.register(Book)


class BookAdmin(admin.ModelAdmin):
    list_display=['name','submitter']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=['name','dob']


# Register your models here.
