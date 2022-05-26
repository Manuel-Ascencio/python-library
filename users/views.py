from django.shortcuts import render
from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsOwnwerOrReadOnly
from rest_framework.decorators import action
from reception.models import Loan
from reception.serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsOwnwerOrReadOnly]

        return [permission() for permission in permission_classes]


    @action(detail=True)
    def my_books(self, request, pk=None):
        queryset = Loan.objects.filter(
            delivery__id = pk
        )
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)