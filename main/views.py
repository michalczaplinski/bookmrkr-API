from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
def bookmarks(request):
    return render(request, 'bookmarks.html')

@ensure_csrf_cookie
def index(request):
    if request.user.is_authenticated():
        return render(request, 'bookmarks.html')
    else:
        return render_to_response("index.html", RequestContext(request, {}))
