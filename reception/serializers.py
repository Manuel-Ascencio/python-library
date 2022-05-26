from rest_framework import serializers
from .models import Loan
from users.serializers import UserSerializer
class BookSerializer(serializers.ModelSerializer):
    # delivery = serializers.CharField(source="get_delivery_barcode_display")
    loan = UserSerializer
    class Meta:
        model = Loan
        fields = "__all__"
        depth = 1