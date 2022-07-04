from django.contrib import admin

# Register your models here.
from bookstore.models import Books, Author, Member


admin.site.register(Author)
admin.site.register(Member)


class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'released_year', 'author', 'paperback']
    search_fields = ['id', 'title', 'released_year', 'author', 'paperback', 'description']
    list_filter = ['id', 'title', 'released_year', 'author', 'paperback']
    list_editable = ['title']

    class Meta:
        model = Books


admin.site.register(Books, BooksAdmin)
