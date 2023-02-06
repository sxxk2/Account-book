import json

import pytest
from rest_framework.reverse import reverse


@pytest.mark.django_db
def test_user_token_refresh_success(client, login):
    access_token, refresh_token = login

    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}
    data = {"refresh": refresh_token}

    response = client.post(reverse("user:token_refresh"), data=data, **headers)

    data = json.loads(response.content)

    assert response.status_code
    assert data["access"]


@pytest.mark.django_db
def test_user_token_refresh_fail_with_invalid_refresh_token(client, login):
    access_token, refresh_token = login

    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}
    data = {"refresh": "invalid_refresh_token"}

    response = client.post(reverse("user:token_refresh"), data=data, **headers)

    data = json.loads(response.content)

    assert response.status_code == 401
    assert data["code"] == "token_not_valid"
    assert data["detail"] == "유효하지 않거나 만료된 토큰"
