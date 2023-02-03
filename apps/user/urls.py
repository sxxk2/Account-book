from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.user.views import SignInView, SignOutView, SignUpView

app_name = "user"

urlpatterns = [
    path("/signup", SignUpView.as_view(), name="user_signup"),
    path("/signin", SignInView.as_view(), name="user_signin"),
    path("/signout", SignOutView.as_view(), name="user_signout"),
    path("/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]
