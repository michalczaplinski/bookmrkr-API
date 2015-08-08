from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bookmarks(request):
    return render(request, 'bookmarks.html')


def index(request):
    return render(request, 'index.html')