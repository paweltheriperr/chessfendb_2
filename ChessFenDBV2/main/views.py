from django.shortcuts import render, HttpResponse
from django.http import Http404

from .models import Fen
from .serializers import FenSerializer
from django.shortcuts import get_object_or_404

from rest_framework import generics

from datetime import datetime


def index(request):
    if request.method == 'POST':
        data = {
            'fen': request.POST['chess-fen'],
            'added': datetime.now(),
        }

        FenSerializer().create(data)

    try:
        fen = Fen.objects.latest('pk')

    except Fen.DoesNotExist:
        fen = None

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