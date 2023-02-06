import json

import pytest
from rest_framework.reverse import reverse


@pytest.mark.django_db
def test_user_signout_success(client, login):
    access_token, refresh_token = login

    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}
    data = {"refresh_token": refresh_token}

    response = client.post(reverse("user:user_signout"), data=data, **headers)

    data = json.loads(response.content)
    assert response.status_code == 200
    assert data["message"] == "로그아웃 되었습니다."


@pytest.mark.django_db
def test_user_signout_fail_with_blacklisted_token(client, login):
    access_token, refresh_token = login

    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}
    data = {"refresh_token": refresh_token}

    logout = client.post(reverse("user:user_signout"), data=data, **headers)

    assert logout.status_code == 200

    response = client.post(reverse("user:user_signout"), data=data, **headers)
    data = json.loads(response.content)
    assert response.status_code == 400
    assert data["message"] == "유효하지 않거나 만료된토큰입니다."


@pytest.mark.django_db
def test_user_signout_fail_with_unauthenticated(client, account):
    response = client.post(reverse("user:user_signout"))
    data = json.loads(response.content)
    assert response.status_code == 401
    assert data["detail"] == "자격 인증데이터(authentication credentials)가 제공되지 않았습니다."
