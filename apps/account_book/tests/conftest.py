import pytest
from rest_framework.reverse import reverse

from apps.account_book.models import AccountBook, AccountBookRecord


@pytest.fixture
def account(django_user_model):
    account = django_user_model.objects.create_user(email="test@gmail.com")
    account.set_password("!test12345678")
    account.save()
    return account


@pytest.fixture
def account_b(django_user_model):
    account = django_user_model.objects.create_user(email="test_b@gmail.com")
    account.set_password("!test12345678")
    account.save()
    return account


@pytest.fixture
def account_book(account, django_user_model):
    user = django_user_model.objects.get(id=account.id)
    account_book = AccountBook.objects.create(user=user, title="test_title")
    return account_book


@pytest.fixture
def account_book_record(account_book):
    account_book = AccountBook.objects.get(id=account_book.id)
    account_book_record = AccountBookRecord.objects.create(
        account_book=account_book, date="2023-01-01", amount=1, description="test_description"
    )
    return account_book_record


@pytest.fixture
def deleted_account_book_record(account_book):
    account_book = AccountBook.objects.get(id=account_book.id)
    deleted_account_book_record = AccountBookRecord.objects.create(
        account_book=account_book, date="2023-01-01", amount=1, description="test_description", is_active=False
    )
    return deleted_account_book_record


@pytest.fixture
def deleted_account_book(account, django_user_model):
    user = django_user_model.objects.get(id=account.id)
    account_book = AccountBook.objects.create(user=user, title="test_title_deleted", is_active=False)
    return account_book


@pytest.fixture
def login(client, account):
    data = {"email": "test@gmail.com", "password": "!test12345678"}

    response = client.post(reverse("user:user_signin"), data=data)

    access_token = response.data["access_token"]
    refresh_token = response.data["refresh_token"]

    return access_token, refresh_token


@pytest.fixture
def login_b(client, account_b):
    data = {"email": "test_b@gmail.com", "password": "!test12345678"}

    response = client.post(reverse("user:user_signin"), data=data)

    access_token = response.data["access_token"]
    refresh_token = response.data["refresh_token"]

    return access_token, refresh_token
