from django import forms

from bookstore.models import Books, Author


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'description', 'released_year', 'paperback', 'author']
