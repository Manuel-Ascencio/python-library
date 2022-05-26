from django.db import models
import uuid
from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
# from reception.models import Loan
# from books.models import BookItem
# Create your models here.

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
    barcode = models.UUIDField(default=uuid.uuid4)
    borrowed = models.DateField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.book} | {self.barcode}"
    
    @property
    def title__barcode(self) -> dict:
        return {
            "number": self.number,
            "barcode": self.barcode
        }



# @receiver(post_save, sender=Loan)
# def update_status_loan(sender, instance, created, **kwargs):
#     if created:
#         loan_item = instance
#         loan_id = loan_item.delivery.id
#         loan = BookItem.objects.get(pk=loan_id)
#         loan.status = False
#         loan.save()