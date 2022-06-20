from django.urls import path

from .views import books_list, books_detail, author_info, books_list_sorted

urlpatterns = [
    path('', books_list, name='books_list'),
    path('bookstore/sorted/<int:author_id>/', books_list_sorted, name='sorted'),
    path('bookstore/author/<int:index_auth>/', author_info, name='author'),
    path('bookstore/<int:index>/', books_detail, name='books_detail'),
]
