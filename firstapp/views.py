from django.http import HttpRequest, HttpResponse
import datetime


def hellodjango(request: HttpRequest):
    return HttpResponse("Hello Django!")


def helloname(request, name):
    return HttpResponse(f"Hello {name}!")


def data(request, data):
    x = datetime.datetime.now()
    try:
        if data == '':
            return HttpResponse(x.strftime('%d.%m.%Y'))
        elif data == 'day':
            return HttpResponse(x.strftime('%d'))
        elif data == 'month':
            return HttpResponse(x.strftime('%m'))
        elif data == 'year':
            return HttpResponse(x.strftime('%Y'))
    except IndexError as error:
        print(error)



#
# def year(request):
#     return HttpResponse("2022")
#
#
# def day(request):
#     return HttpResponse("22")
#
#
# def month(request):
#     return HttpResponse("03")
