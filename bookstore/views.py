from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404

# Create your views here.
from django.views import View

from bookstore.forms import BooksForm, ReviewForm
from bookstore.models import Books, Author, ReviewBook

menu = [{'title': "Book list", 'url_name': 'books_list'},
        {'title': "Add book", 'url_name': 'add_book'},
]


class BooksView(View):
    def post(self, request):
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
        books = Books.objects.all().order_by('-id')
        context = {'books': books, 'post_form': BooksForm}
        return render(request, 'bookstore/books_list.html', context=context)

    def get(self, request):
        books = Books.objects.all().order_by('-id')
        if request.method == "GET" and 'qwerty' in request.GET:
            qwerty = request.GET['qwerty']
            books = books.filter(title__icontains=qwerty)
        context = {'books': books, 'post_form': BooksForm}
        return render(request, 'bookstore/books_list.html', context=context)


def books_detail(request, index):
    book = get_object_or_404(Books, pk=index)
    reviews = ReviewBook.objects.filter(book=book)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rev = form.save(commit=False)
            rev.user = request.user
            rev.book = book
            rev.save()
    else:
        form = ReviewForm()
    context = {'book': book, 'rev_form': form, 'reviews': reviews}
    return render(request, 'bookstore/books_detail.html', context=context)


def author_info(request, index):
    author = get_object_or_404(Author, pk=index)
    context = {'author': author}
    return render(request, 'bookstore/author.html', context=context)


def books_list_sorted(request, index):
    books = get_list_or_404(Books, author=index)
    context = {'books': books}
    return render(request, 'bookstore/books_list_sorted.html', context=context)


class AddBookView(View):
    def post(self, request):
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            books = Books.objects.all().order_by('-id')
        context = {'books': books, 'post_form': BooksForm}
        return render(request, 'bookstore/add_book.html', context=context)

    def get(self, request):
        books = Books.objects.all().order_by('-id')
        if request.method == "GET" and 'qwerty' in request.GET:
            qwerty = request.GET['qwerty']
            books = books.filter(title__icontains=qwerty)
        context = {'books': books, 'post_form': BooksForm}
        return render(request, 'bookstore/add_book.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Sorry. Page not found</h1>')
