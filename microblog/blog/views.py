from django.shortcuts import render

from blog.models import Book, Readers


def books_list(request):
    books = Book.objects.order_by('-publication_year', 'title')

    context = {
        'books': books,
    }

    return render(request, 'blog/books.html', context=context)


def readers_list(request):
    readers = Reader.objects.all()

    context = {
        'readers': readers
    }

    return render(request, 'blog/readers.html',context=context)