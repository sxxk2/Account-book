from django.urls import path

from apps.user.views import SignInView, SignOutView, SignUpView

app_name = "user"

urlpatterns = [
    path("/signup", SignUpView.as_view(), name="user_signup"),
    path("/signin", SignInView.as_view(), name="user_signin"),
    path("/signout", SignOutView.as_view(), name="user_signout"),
]
