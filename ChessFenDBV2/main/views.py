from django.shortcuts import render, HttpResponse
from .models import Fen


def index(request):
    yes = Fen.objects.all()
    return HttpResponse('<h1>Siur</h1>')
