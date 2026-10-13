from django.shortcuts import render
from django.http import HttpResponse


def agust(request):
    return HttpResponse("Its, Agust page")


def sep(request):
    return HttpResponse("Its, September page")

def march(request):
    return HttpResponse("Its, March page")