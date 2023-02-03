from django.urls import path

from apps.user.views import SignUpView

app_name = "user"

urlpatterns = [path("/signup", SignUpView.as_view(), name="user_signup")]
