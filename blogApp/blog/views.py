from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'Harsha',
        'title': 'Blog post 1',
        'content': 'This is a test blog post',
        'date_posted': 'March 25, 2020'
    },
    {
        'author': 'Anu',
        'title': 'Blog post 2',
        'content': 'This is a second test blog post',
        'date_posted': 'March 26, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):

    return render(request, 'blog/about.html', {'title': 'About'})
