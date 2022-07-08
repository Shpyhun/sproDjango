from django import forms

from bookstore.models import Books, ReviewBook


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'description', 'released_year', 'paperback', 'author']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewBook
        fields = ['text']
