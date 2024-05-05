from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("demo index")

def page3(request):
    return HttpResponse("page3")
