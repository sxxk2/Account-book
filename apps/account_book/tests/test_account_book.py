import json

from rest_framework.reverse import reverse


def test_account_book_create_success(client, login):
    url = reverse("account_book:account_book")
    access_token, refresh_token = login

    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}
    data = {
        "title": "test_title",
        "balance": 1,
    }
    response = client.post(url, data=data, **headers)

    data = json.loads(response.content)

    assert response.status_code == 201
    assert data["title"] == "test_title"
    assert data["balance"] == 1


def test_account_book_create_fail_with_unauthenticated(client):
    url = reverse("account_book:account_book")
    access_token = "invalid_token"
    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}

    data = {"title": "test_title", "balance": 1}
    response = client.post(url, data=data, **headers)

    data = json.loads(response.content)

    assert response.status_code == 401


def test_account_book_create_fail_with_no_data(client, login):
    url = reverse("account_book:account_book")
    access_token, refresh_token = login
    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}

    data = {}
    response = client.post(url, data=data, **headers)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["title"][0] == "이 필드는 필수 항목입니다."


def test_account_book_list_read_success(client, account_book, login):
    url = reverse("account_book:account_book")

    access_token, refresh_token = login
    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}

    response = client.get(url, **headers)

    data = json.loads(response.content)

    assert response.status_code == 200
    assert data[0]["title"] == "test_title"
    assert data[0]["balance"] == 0


def test_account_book_list_read_fail_with_no_authentication(client):
    url = reverse("account_book:account_book")

    access_token = None
    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}

    response = client.get(url, **headers)

    data = json.loads(response.content)

    assert response.status_code == 401
    assert data["detail"] == "이 토큰은 모든 타입의 토큰에 대해 유효하지 않습니다"
