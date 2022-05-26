from django.db import models
from books.models import BookItem
from users.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
# Create your models here.


class Loan(models.Model):
    delivery = models.ForeignKey(BookItem, on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    name = "nombre"

    def __str__(self):
        return f"{self.person.email} | {self.delivery.book.title}"


@receiver(post_save, sender=Loan)
def update_status_loan(sender, instance, created, **kwargs):
    if created:
        loan_item = instance
        loan_id = loan_item.delivery.id
        loan = BookItem.objects.get(pk=loan_id)
        loan.status = False
        loan.save()

@receiver(post_delete, sender=Loan)
def update_status_loan(sender, instance, **kwargs):
    loan_item = instance
    loan_id = loan_item.delivery.id
    loan = BookItem.objects.get(pk=loan_id)
    loan.status = True
    loan.save()