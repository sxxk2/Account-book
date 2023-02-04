from django.contrib import admin
from django.urls import include, path

from apps.utils.url_shortener import URLShortenerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/shortener", URLShortenerView.as_view()),
    path("api/users", include("apps.user.urls")),
    path("api/account-books", include("apps.account_book.urls")),
]
