import pytest


@pytest.fixture
def account(django_user_model):
    account = django_user_model.objects.create_user(email="test@gmail.com")
    account.set_password("!test12345678")
    account.save()
    return account
