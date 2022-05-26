from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title", "author", "subject", "category"]

