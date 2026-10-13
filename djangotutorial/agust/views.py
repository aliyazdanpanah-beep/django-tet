from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Dynamic URLs insted astatic URLs

def handel_month(reguest, month):
    challeng_text = None

    if month == "agust":
        challeng_text = "Its, Agust page"
    elif month == "sep":
        challeng_text = "Its, September page"
    elif month == "march":
        challeng_text = "Its, March page"
    else:
        return HttpResponseNotFound("This month is not supported")

    return HttpResponse(challeng_text)