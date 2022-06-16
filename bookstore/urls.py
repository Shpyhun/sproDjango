from django.urls import path

from .views import books_list, books_detail, author_info, books_list_sorted

urlpatterns = [
    path('bookstore/', books_list, name='books_list'),
    path('bookstore/sorted', books_list_sorted, name='books_list_sorted')
    path('bookstore/author/<str:index_auth>/', author_info, name='author'),
    # path('bookstore/<str:index>/<str:index_auth>/', author_info, name='author'),
    path('bookstore/<str:index>/', books_detail, name='books_detail'),
]
