from django.urls import path

from .views import books_detail, author_info, books_list_sorted, BooksView, AddBookView

urlpatterns = [
    path('', BooksView.as_view(), name='books_list'),
    path('bookstore/sorted/<int:index>/', books_list_sorted, name='sorted'),
    path('bookstore/author/<int:index>/', author_info, name='author'),
    path('bookstore/<int:index>/', books_detail, name='books_detail'),
    path('bookstore/add_book/', AddBookView.as_view(), name='add_book'),
]
