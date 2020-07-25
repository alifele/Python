from django.shortcuts import render
from django.http import HttpResponse
from .models import Post



posts = [
    {
    'author':'Ali Fele Paranj',
    'title':"About me",
    'content':'My name is ali fele paranj living in Iran',
    'date_posted':'August'
    },
    {
    'author':'Elahe',
    'title':"More On me",
    'content':'Hello there how are you?',
    'date_posted':'September'
    },
    {
    'author':'Elahe',
    'title':"More On me",
    'content':'Hello there how are you?',
    'date_posted':'September'
    }
]

title = 'ali'

# Create your views here.


def home(request):
    context = {
    #'posts':posts,
    'posts':Post.objects.all(),
    'title':title
    }
    return render(request,'blog/home.html', context)


def subhome(request):
    return render(request,'blog/about.html')
