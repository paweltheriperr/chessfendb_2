from django.urls import path
from .views import index, FenList, FenDetail


urlpatterns = [
    path('', index, name='index'),
    path('fens/', FenList.as_view(), name='fens'),
    path('fens/<int:pk>/', FenDetail.as_view(), name='fen_detail'),
]
