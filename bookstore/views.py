from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404

# Create your views here.
from bookstore.forms import BooksForm
from bookstore.models import Books, Author


def books_list(request):
    books = Books.objects.all()
    if request.method == "GET" and 'qwerty' in request.GET:
        qwerty = request.GET['qwerty']
        books = books.filter(title__icontains=qwerty)
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            books = Books.objects.all().order_by('-id')
    context = {'books': books, 'post_form': BooksForm}
    return render(request, 'bookstore/books_list.html', context=context)


def books_detail(request, index):
    book = get_object_or_404(Books, pk=index)
    context = {'book': book}
    return render(request, 'bookstore/books_detail.html', context=context)


def author_info(request, index):
    author = get_object_or_404(Author, pk=index)
    context = {'author': author}
    return render(request, 'bookstore/author.html', context=context)


def books_list_sorted(request, index):
    books = get_list_or_404(Books, author=index)
    context = {'books': books}
    return render(request, 'bookstore/books_list_sorted.html', context=context)


def add_book(request):
    books = Books.objects.all()
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            books = Books.objects.all()
    context = {'books': books, 'post_form': BooksForm}
    return render(request, 'bookstore/add_book.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Sorry. Page not found</h1>')
