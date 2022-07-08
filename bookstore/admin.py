
from django.contrib import admin

# Register your models here.
from bookstore.models import Books, Author, ReviewBook


admin.site.register(Author)


class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'released_year', 'author', 'paperback']
    search_fields = ['id', 'title', 'released_year', 'author', 'paperback', 'description']
    list_filter = ['id', 'title', 'released_year', 'author', 'paperback']
    list_editable = ['title']

    class Meta:
        model = Books


admin.site.register(Books, BooksAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'book']
    search_fields = ['id', 'text', 'book', 'author']
    list_filter = ['id', 'text', 'book']
    list_editable = ['text']

    class Meta:
        model = ReviewBook


admin.site.register(ReviewBook, ReviewAdmin)
