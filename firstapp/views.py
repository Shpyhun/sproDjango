import datetime

from django.http import HttpRequest, HttpResponse, HttpResponseNotFound


def hellodjango(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello Django!")


def helloname(request, name) -> HttpResponse:
    return HttpResponse(f"Hello {name}!")


def fulldate(request: HttpRequest) -> HttpResponse:
    current_date = datetime.datetime.now()
    return HttpResponse(current_date.strftime('%d.%m.%Y'))


def date(request, index):
    x = datetime.datetime.now()
    if index == 'day':
        return HttpResponse(x.strftime('%d'))
    elif index == 'month':
        return HttpResponse(x.strftime('%m'))
    elif index == 'year':
        return HttpResponse(x.strftime('%Y'))
    else:
        return HttpResponseNotFound(f'Page {index} not found')
