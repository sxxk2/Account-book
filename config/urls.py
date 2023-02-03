from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users", include("apps.user.urls")),
    path("api/account-books", include("apps.account_book.urls")),
]
