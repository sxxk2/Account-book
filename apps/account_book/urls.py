from django.urls import path

from apps.account_book.views import (
    AccountBookDetailView,
    AccountBookView,
    DeletedAccountBookRestoreView,
    DeletedAccountBookView,
)

app_name = "account_book"

urlpatterns = [
    path("", AccountBookView.as_view(), name="account_book"),
    path("/deleted", DeletedAccountBookView.as_view(), name="deleted_account_book"),
    path("/deleted/<int:pk>", DeletedAccountBookRestoreView.as_view(), name="deleted_account_book"),
    path("/<int:pk>", AccountBookDetailView.as_view(), name="account_book_detail"),
]
