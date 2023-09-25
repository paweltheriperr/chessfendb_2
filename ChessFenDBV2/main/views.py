from django.shortcuts import render, HttpResponse
from django.http import Http404

from .models import Fen
from .serializers import FenSerializer
from django.shortcuts import get_object_or_404
# biblioteka do errorów
from rest_framework import generics


def index(request):
    try:
        fen = get_object_or_404(Fen)  # Spróbuj pobrać obiekt Fen
    except Fen.DoesNotExist:
        fen = None  # Jeśli nie ma obiektu Fen, ustaw fen na None

    return render(request, 'main/main.html', {'fen': fen})


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