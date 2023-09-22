from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Fen
from .serializers import FenSerializer

from rest_framework.parsers import JSONParser


def index(request):
    yes = Fen.objects.all()
    return HttpResponse('<h1>Siur</h1>')


@csrf_exempt
def fen_list(request):
    if request.method == 'GET':
        fen = Fen.objects.all()
        serializer = FenSerializer(fen, many=True)

        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def fen_detail(request, pk):
    try:
        fen = Fen.objects.get(pk=pk)

    except Fen.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FenSerializer(fen)

        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FenSerializer(fen, data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)

    if request.method == 'DELETE':
        fen.delete()

        return HttpResponse(status=204)

def daily_task(request):
    pass


def display_chessboard(request):
    pass