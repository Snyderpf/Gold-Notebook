
from django.http import HttpResponse
from django.shortcuts import render

def movies(request):
    data = {
        'movies' : [
        {
            'id':5,
            'title':' Jaws',
            'year' : '1969'
        },
        {
            'id':6,
            'title':' Mationa',
            'year' : '1876'

        },
        {'id':6,
            'title':'Americano',
            'year' : '1231'
        }
        ]
    }
    return render(request, 'movies/movies.html', data)
    # return HttpResponse("Hello there")

def home(request):
    # return render(request,)
    return HttpResponse("Home Page You are welcomde to my lovely abode")