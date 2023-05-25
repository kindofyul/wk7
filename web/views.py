from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib import auth
from django.contrib.auth.models import User
import os

def home(request):
    movies = Movie.objects.all()
    count = len(movies)
    ctx = {
        'movies': movies,
        'count': count,
    }
    return render(request, "home.html", ctx)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'detail.html', {'movie':movie})

def create(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    elif request.method == 'POST':
        movie = Movie()
        movie.title = request.POST['title']
        movie.author = request.user
        movie.r_rate = float(request.POST['r_rate'])
        movie.status = True if request.POST.get('status', None) == 'on' else False
        movie.review = request.POST['review']
        movie.image = request.FILES.get('image')
        movie.save()
        return redirect('detail', movie.id)
    return render(request, 'create.html')

def edit(request, movie_id):
    edit_movie = Movie.objects.get(pk = movie_id)
    return render(request, 'edit.html', {'movie':edit_movie})

def update(request, movie_id):
    update_movie = Movie.objects.get(pk = movie_id)
    update_movie.title = request.POST['title']
    update_movie.r_rate = float(request.POST['r_rate'])
    update_movie.status = True if request.POST.get('status', None) == 'on' else False
    update_movie.review = request.POST['review']
    update_movie.image = request.FILES.get('image')
    update_movie.save()
    return redirect('detail', update_movie.id)

def delete(request, movie_id):
    delete_movie = Movie.objects.get(pk = movie_id)
    delete_movie.delete()
    return redirect(home)

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    
    if request.method == "POST":
        userid = request.POST['username']
        userpw = request.POST['password']

        user = auth.authenticate(request, username=userid, password=userpw)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        
        else:
            return render(request, 'login.html')
        
def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        userid = request.POST['username']
        userpw = request.POST['password']
        new_user = User.objects.create_user(username=userid, password=userpw)
        auth.login(request, new_user)
        return redirect('home')