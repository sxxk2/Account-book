import json

from rest_framework.reverse import reverse


def test_account_book_detail_read_success(client, account_book, login):
    url = reverse("account_book:account_book_detail", kwargs={"pk": account_book.id})

    access_token, refresh_token = login
    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}

    response = client.get(url, **headers)
    data = json.loads(response.content)

    assert response.status_code == 200
    assert data["title"] == "test_title"
    assert data["balance"] == 0
    assert data["is_active"] == True


def test_account_book_detail_read_fail_with_unauthorized_user(client, account_book, login_b):
    url = reverse("account_book:account_book_detail", kwargs={"pk": account_book.id})

    access_token, refresh_token = login_b
    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}

    response = client.get(url, **headers)
    data = json.loads(response.content)

    assert response.status_code == 403
    assert data["detail"] == "이 작업을 수행할 권한(permission)이 없습니다."


def test_account_book_detail_update_success(client, account_book, login):
    url = reverse("account_book:account_book_detail", kwargs={"pk": account_book.id})

    access_token, refresh_token = login
    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}
    data = {"balance": 111, "title": "updated_title"}
    response = client.patch(url, data=data, content_type="application/json", **headers)
    data = json.loads(response.content)

    assert response.status_code == 200
    assert data["title"] == "updated_title"
    assert data["balance"] == 111
    assert data["updated_at"]


def test_account_book_detail_update_fail_with_no_data(client, account_book, login):
    url = reverse("account_book:account_book_detail", kwargs={"pk": account_book.id})

    access_token, refresh_token = login
    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}
    data = {
        # "balance": 111,
        # "title": "updated_title"
    }
    response = client.patch(url, data=data, content_type="application/json", **headers)
    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["non_field_errors"][0] == "입력값이 없습니다."


def test_account_book_detail_delete_success(client, account_book, login):
    url = reverse("account_book:account_book_detail", kwargs={"pk": account_book.id})

    access_token, refresh_token = login
    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}
    response = client.delete(url, **headers)
    data = json.loads(response.content)

    assert response.status_code == 200
    assert data["is_active"] == False
    assert data["deleted_at"]


def test_account_book_detail_delete_fail_with_deleted_account_book(client, deleted_account_book, login):
    url = reverse("account_book:account_book_detail", kwargs={"pk": deleted_account_book.id})

    access_token, refresh_token = login
    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}
    response = client.delete(url, **headers)
    data = json.loads(response.content)

    assert response.status_code == 400
    assert data[0] == "이미 삭제된 가계부 입니다."
