from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Book, Author

def home(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    return render(request, 'home.html', {'books':books,'authors':authors})

def book_detail(request, book_id):
    try:
        book=Book.objects.get(book_id=book_id)
    except Book.DoesNotExist:
        raise Http404('Book not found')
    return render(request, 'book_detail.html',{'book':book,})
def about(request):
    return render(request, 'about.html', {'title':'About us'})

# Create your views here.
