from django.urls import path

from apps.account_book.views import AccountBookDetailView, AccountBookView

app_name = "account_book"

urlpatterns = [
    path("", AccountBookView.as_view(), name="account_book"),
    path("/<int:pk>", AccountBookDetailView.as_view(), name="account_book_detail"),
]
