from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


# def home(request):
#     return HttpResponse('<h1>Welcome to Home Page</h1>')

# def home(request):
#     return render(request, 'home.html', {'name': 'Greg'})

def home(request):
    searchTerm = request.GET.get('searchMovie')
    movies = Movie.objects.all()
    return render(request, 'home.html',
                  {'searchTerm': searchTerm, 'movies': movies})


def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})


def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')
