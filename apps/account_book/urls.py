from django.urls import path

from apps.account_book.views import AccountBookView

app_name = "account_book"

urlpatterns = [
    path("", AccountBookView.as_view(), name="account_book"),
]
