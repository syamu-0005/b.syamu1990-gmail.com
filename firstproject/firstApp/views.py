from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def display_view(request):
    s = '<h1>Hello students welcome to durga soft Django classes!!!</h1>'
    return HttpResponse(s)
