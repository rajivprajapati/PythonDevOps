from django.shortcuts import render
from django.http import HttpResponse, request
from django.http import Http404

# Create your views here.

def index(request):
    return render(request, "todo/index.html")

def view_404(request):
    raise Http404("Page not found")
