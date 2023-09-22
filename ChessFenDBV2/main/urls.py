from django.urls import path
from .views import index, fen_list, fen_detail


urlpatterns = [
    path('', index, name='index'),
    path('fens/', fen_list, name='fens'),
    path('fens/<int:pk>/', fen_detail, name='fen_detail'),
]
