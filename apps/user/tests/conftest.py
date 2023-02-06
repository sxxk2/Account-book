import pytest
from rest_framework.reverse import reverse


@pytest.fixture
def account(django_user_model):
    account = django_user_model.objects.create_user(email="test@gmail.com")
    account.set_password("!test12345678")
    account.save()
    return account


@pytest.fixture
def login(client, account):
    data = {"email": "test@gmail.com", "password": "!test12345678"}

    response = client.post(reverse("user:user_signin"), data=data)

    access_token = response.data["access_token"]
    refresh_token = response.data["refresh_token"]

    return access_token, refresh_token
