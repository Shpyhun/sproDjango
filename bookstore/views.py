from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

books = [
    {
        'id': 1,
        'title': 'Django for APIs: Build web APIs with Python & Django',
        'released_year': 'Publication date: 15 Jun. 2018',
        'description': 'The author has done a job explaining how to create REST ful APIs using Django and the Django '
                       'REST framework – from scratch and of different complexity levels. This is not a basic '
                       'book that will teach you “What is Django”, instead this is for developers who want to write '
                       'codeAPIs that can be reused. The book focuses more on the Django REST framework and React and '
                       'how you can build APIs easily and by using best coding practices. If you are overwhelmed by '
                       'the official documentation and tutorials, this book is a good  relief and covers only the '
                       'most important concepts. The book is written for beginners but the author also points to '
                       'many useful resources if you want to get into more complicated models.',
        'author_id': 1,
        'paperback': 'Print length: 190 pages',
    },
    {
        'id': 2,
        'title': 'Two Scoops of Django 1.11: Best Practices for the Django Web Framework',
        'released_year': 'Publication date: 30 Jun. 2017',
        'description': 'If you have worked on a Django project before and want to properly learn the framework, '
                       'this is the best book. It is written keeping in mind both beginners and advanced level '
                       'professionals. It is your go-to reference guide for tips and valuable suggestions for best '
                       'practices. There are plenty of funny but informative diagrams that keep you hooked on the '
                       'book and the authors have maintained a friendly tone for writing as well. The best part of '
                       'the book is that you can skip chapters and read them as you like. Each chapter is independent '
                       'of others. You would also learn to deploy your application to the cloud (PaaS). The authors’ '
                       'experience clearly shows up with the wealth of information they have shared in the form of '
                       'tips, code samples, tricks, and techniques.',
        'author_id': 2,
        'paperback': 'Paperback: 555 pages',
    },
    {
        'id': 3,
        'title': 'Django for Professionals: Production websites with Python & Django',
        'released_year': 'Publication date: 21 July 2019',
        'description': 'This is an extension of the Django for beginners’ book. While in the basic version, you would '
                       'build simple websites that are focused on the understanding of concepts, this book focuses on '
                       'more complex real-life applications and projects and is written keeping that in mind. The '
                       'author gives you lots of tips and techniques that you need when you build production apps. As '
                       'you read each chapter, you will appreciate the choice of other tools by the author more and '
                       'more. You will need a basic understanding of Python, but that is it. The author assumes you '
                       'do not know any others – Bootstrap, PostgreSQL, Docker, etc… He also chooses to build a '
                       'website that covers all the concepts that you will ever need to become a pro in Django.',
        'author_id': 1,
        'paperback': 'Print length: 380 pages',
    },
    {
        'id': 4,
        'title': 'Django 2 by Example',
        'released_year': 'Publication date: 31 May 2018',
        'description': 'The book is good for beginners and intermediate level learners. If you have worked with '
                       'JavaScript, HTML, and Python, this book would be a great choice. It starts from building a '
                       'web application from scratch and covers even the most advanced topics in-depth, '
                       'including integration with other technologies like Celery and Redis. The author covers a '
                       'wide range of topics and provides a lot of code examples. However, not each line of code is '
                       'explained and you may want to keep the official Django documentation open to understand more '
                       'about some methods and steps. This is good – because you get to learn more than you would '
                       'expect and in a flow. It is also a good option to read basics about Django before you start '
                       'the book, just for a heads-up – even otherwise, the author assumes you have no prior '
                       'knowledge of Django.',
        'author_id': 3,
        'paperback': 'Print length: 526 pages',
    },
    {
        'id': 5,
        'title': 'Django Unleashed',
        'released_year': 'Publication date: 19 Nov. 2015',
        'description': 'This is a good book for beginners as well as Django programmers with about 4-5 years who '
                       'would like to learn more. The book is a detailed guide and starts with scratch to build '
                       'applications in Django. It explains various ways of solving the same problem and then '
                       'explains which one is better too. The author takes it slowly from basics to complex topics '
                       'and though some advanced topics may be a bit difficult to follow initially, once you practice '
                       'them, you will appreciate the effort the author has put to explain them. Complex topics like '
                       'Generic views, creating custom users and managers, security, performance, etc are explained '
                       'very nicely.',
        'author_id': 4,
        'paperback': 'Print length: 840 pages',
    },
]

authors = [
    {
        'id': 1,
        'first_name': 'William',
        'last_name': 'Vincent',
        'age': 43,
    },
    {
        'id': 2,
        'first_name': 'Daniel',
        'last_name': 'Greenfeld',
        'age': 46,
    },
    {
        'id': 3,
        'first_name': 'Antonio',
        'last_name': 'Mele',
        'age': 38,
    },
    {
        'id': 4,
        'first_name': 'Andrew',
        'last_name': 'Pinkham',
        'age': 33,
    },
]


def books_list(request):
    return render(request, 'bookstore/books_list.html', context={'books': books})


def books_detail(request, index):
    try:
        book = books[int(index) - 1]
        return render(request, 'bookstore/books_detail.html', context=book)
    except IndexError:
        return HttpResponseNotFound(f'non found {index}')


def author_info(request, index_auth):
    author = authors[int(index_auth) - 1]
    return render(request, 'bookstore/author.html', context=author)


def books_list_sorted(request, author_id):
    # new_books = [book for book in books if book['author_id'] == author_id]
    new_books = []
    for book in books:
        if book['author_id'] == author_id:
            new_books.append(book)

    return render(request, 'bookstore/books_list_sorted.html', context={'books': new_books})


