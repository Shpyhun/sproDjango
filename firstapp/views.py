from django.http import HttpRequest, HttpResponse


def hellodjango(request: HttpRequest):
    return HttpResponse("Hello Django!")


def helloname(request, name):
    return HttpResponse(f"Hello {name}!")


def data(request):
    return HttpResponse("22.03.22")


def year(request):
    return HttpResponse("2022")


def day(request):
    return HttpResponse("22")


def month(request):
    return HttpResponse("03")
