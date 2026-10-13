from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Dynamic URLs insted astatic URLs

challeng_text = {
    "agust": "Its, Agust page",
    "sep": "Its, September page",
    "march": "Its, March page",
}

def handel_month(reguest, month):
    
    try:
        monthly_named = challeng_text[month] 
        return HttpResponse(monthly_named)
    except:
        return HttpResponseNotFound("This month is not support")



def handel_month_by_number(request, month):
    return HttpResponse(month)