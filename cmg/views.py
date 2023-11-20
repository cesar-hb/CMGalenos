from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request, "cmg/home.html")