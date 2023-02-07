from django.urls import path

from apps.account_book.views import (
    AccountBookDetailView,
    AccountBookRecordDetailView,
    AccountBookRecordView,
    AccountBookView,
    DeletedAccountBookRestoreOrHardDeleteView,
    DeletedAccountBookView,
)

app_name = "account_book"

urlpatterns = [
    path("", AccountBookView.as_view(), name="account_book"),
    path("/deleted", DeletedAccountBookView.as_view(), name="deleted_account_book"),
    path(
        "/deleted/<int:pk>",
        DeletedAccountBookRestoreOrHardDeleteView.as_view(),
        name="deleted_account_book_restore_or_hard_delete",
    ),
    path("/<int:pk>", AccountBookDetailView.as_view(), name="account_book_detail"),
    path("/<int:pk>/records", AccountBookRecordView.as_view(), name="account_book_record"),
    path("/<int:pk>/records/<int:record_pk>", AccountBookRecordDetailView.as_view(), name="account_book_record_detail"),
]
