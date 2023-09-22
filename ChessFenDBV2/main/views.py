from django.shortcuts import render, HttpResponse
from django.http import Http404

from .models import Fen
from .serializers import FenSerializer

from rest_framework import generics


def index(request):
    yes = Fen.objects.all()
    return HttpResponse('<h1>Siur</h1>')


class FenList(generics.ListCreateAPIView):
    queryset = Fen.objects.all()
    serializer_class = FenSerializer


class FenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fen.objects.all()
    serializer_class = FenSerializer


def daily_task(request):
    pass


def display_chessboard(request):
    pass