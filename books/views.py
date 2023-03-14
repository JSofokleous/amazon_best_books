from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):

    books = Book.objects.all()

    good_books = []
    for book in books:
        if int(book.ratings_total) >= 400:
            good_books.append(book)
    
    return render(request, 'books/index.html', {"good_books": books})

def library(request):
    return render(request, 'books/library.html')
