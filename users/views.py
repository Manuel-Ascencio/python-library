from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from books.models import Book
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsOwner
from books.serializers import BookSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwner]


    @action(detail=True)
    def my_rent_books(self, request, pk):
        books = Book.objects.filter(
            booitem__rent=pk
        )
        serializer = BookSerializer(books, many=True)
        try:
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_200_OK)



    @action(detail=True)
    def my_reserve_books(self, request, pk):
        books = Book.objects.filter(
            booitem__reserve=pk
        )
        serializer = BookSerializer(books, many=True)
        try:
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_200_OK)