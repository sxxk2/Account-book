import json

import pytest
from rest_framework.reverse import reverse


def test_user_signin_success(client, account):
    url = reverse("user:user_signin")

    data = {"email": "test@gmail.com", "password": "!test12345678"}

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 200
    assert data["message"] == "로그인 되었습니다."
    assert data["access_token"]
    assert data["refresh_token"]


@pytest.mark.django_db
def test_user_signin_fail_with_invalid_email(client):
    url = reverse("user:user_signin")

    data = {"email": "not_exist_account@gmail.com", "password": "!test12345678"}

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["non_field_errors"][0] == "아이디 또는 비빌먼호를 잘못 입력했습니다."


@pytest.mark.django_db
def test_user_signin_fail_with_invalid_password(client, account):
    url = reverse("user:user_signin")

    data = {"email": "test@gmail.com", "password": "incorrect_password"}

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["non_field_errors"][0] == "아이디 또는 비밀번호를 잘못 입력했습니다."


@pytest.mark.django_db
def test_user_signin_fail_with_invalid_email_and_password(client):
    url = reverse("user:user_signin")

    data = {"email": "not_exist_account@gmail.com", "password": "incorrect_password"}

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["non_field_errors"][0] == "아이디 또는 비빌먼호를 잘못 입력했습니다."


@pytest.mark.django_db
def test_user_signin_fail_with_no_email(client):
    url = reverse("user:user_signin")

    data = {
        # "email": "not_exist_account@gmail.com",
        "password": "incorrect_password"
    }

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["email"][0] == "이 필드는 필수 항목입니다."


@pytest.mark.django_db
def test_user_signin_fail_with_no_password(client):
    url = reverse("user:user_signin")

    data = {
        "email": "not_exist_account@gmail.com",
        # "password": "incorrect_password"
    }

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["password"][0] == "이 필드는 필수 항목입니다."


@pytest.mark.django_db
def test_user_signin_fail_with_no_email_and_password(client):
    url = reverse("user:user_signin")

    data = {
        # "email": "not_exist_account@gmail.com",
        # "password": "incorrect_password"
    }

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["email"][0] == "이 필드는 필수 항목입니다."
    assert data["password"][0] == "이 필드는 필수 항목입니다."
