import json

import pytest
from rest_framework.reverse import reverse


@pytest.mark.django_db
def test_user_signup_success(client):
    url = reverse("user:user_signup")

    data = {"email": "test_register@gmail.com", "password": "!test12345678"}

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 201
    assert data["message"] == "회원가입에 성공했습니다."


@pytest.mark.django_db
def test_user_signup_fail_with_invalid_email_format(client):
    url = reverse("user:user_signup")

    data = {"email": "not_match_to_email_foramt", "password": "!test12345678"}

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["email"][0] == "유효한 이메일 주소를 입력하십시오."


@pytest.mark.django_db
def test_user_signup_fail_with_existed_email(client, account):
    url = reverse("user:user_signup")

    data = {"email": "test@gmail.com", "password": "!test12345678"}

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["email"][0] == "user의 email은/는 이미 존재합니다."


@pytest.mark.django_db
def test_user_signup_fail_with_invalid_password(client):
    url = reverse("user:user_signup")

    data = {"email": "test_register@gmail.com", "password": "not_match_to_regex"}

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["non_field_errors"][0] == "문자, 숫자, 기호를 조합하여 8자 이상을 사용하세요."


@pytest.mark.django_db
def test_user_signup_fail_with_no_email(client):
    url = reverse("user:user_signup")

    data = {
        # "email": "test_register@gmail.com",
        "password": "!test12345678"
    }

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["email"][0] == "이 필드는 필수 항목입니다."


@pytest.mark.django_db
def test_user_signup_fail_with_no_password(client):
    url = reverse("user:user_signup")

    data = {
        "email": "test_register@gmail.com",
        # "password": "!test12345678"
    }

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["password"][0] == "이 필드는 필수 항목입니다."


@pytest.mark.django_db
def test_user_signup_fail_with_no_email_and_password(client):
    url = reverse("user:user_signup")

    data = {
        # "email": "test_register@gmail.com",
        # "password": "!test12345678"
    }

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["email"][0] == "이 필드는 필수 항목입니다."
    assert data["password"][0] == "이 필드는 필수 항목입니다."
