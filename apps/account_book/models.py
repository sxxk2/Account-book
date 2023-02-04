from django.db import models

from apps.user.models import User
from apps.utils.timestamp import TimeStampedModel


class AccountBook(TimeStampedModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="account_book")
    title = models.CharField(max_length=20)
    balance = models.IntegerField(default=0)
    is_active = models.BooleanField("삭제 여부", default=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "account_books"


class AccountBookRecord(TimeStampedModel):
    account_book = models.ForeignKey(to=AccountBook, on_delete=models.CASCADE, related_name="account_book_record")
    amount = models.IntegerField("금액")
    description = models.CharField(max_length=100)
    date = models.DateField()
    is_active = models.BooleanField("삭제 여부", default=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.description} : {self.amount}"

    class Meta:
        db_table = "account_book_records"
