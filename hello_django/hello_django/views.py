from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    return render(request, 'about.html', {'greating': 'hello'})


def reverse(request):
    user_text = request.GET['username']
    rev = user_text[::-1]
    return render(request, 'reverse.html', {'word': rev})


def home(request):
    return HttpResponse('This is my home')