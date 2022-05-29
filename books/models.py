from django.db import models
import uuid
from users.models import User


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    @property
    def title_author(self):
        return f"{self.title} | {self.author}"



class BookItem(models.Model):
    barcode = models.UUIDField(default=uuid.uuid4, editable=False)
    borrowed = models.DateField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rack = models.CharField(max_length=4)
    reserve = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True, related_name="reserve")
    is_resrve = models.BooleanField(default=False)
    rent = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True, related_name="rent")
    is_rent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book} | {self.rack}"
    
    @property
    def title__barcode(self) -> dict:
        return {
            "number": self.number,
            "barcode": self.barcode
        }

