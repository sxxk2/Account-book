import json

from rest_framework.reverse import reverse


def test_deleted_account_book_delete_success(client, deleted_account_book, login):
    url = reverse("account_book:deleted_account_book_restore_or_hard_delete", kwargs={"pk": deleted_account_book.id})

    access_token, refresh_token = login
    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}

    response = client.delete(url, **headers)

    assert response.status_code == 204


def test_deleted_account_book_delete_fail_with_not_deleted_account_book(client, account_book, login):
    url = reverse("account_book:deleted_account_book_restore_or_hard_delete", kwargs={"pk": account_book.id})

    access_token, refresh_token = login
    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}

    response = client.delete(url, **headers)
    data = json.loads(response.content)

    assert response.status_code == 404
    assert data["detail"] == "찾을 수 없습니다."


def test_deleted_account_book_update_success(client, deleted_account_book, login):
    url = reverse("account_book:deleted_account_book_restore_or_hard_delete", kwargs={"pk": deleted_account_book.id})

    access_token, refresh_token = login
    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}

    response = client.patch(url, **headers)

    data = json.loads(response.content)

    assert response.status_code == 200
    assert data["is_active"] == True


def test_deleted_account_book_update_fail_with_not_deleted_account_book(client, account_book, login):
    url = reverse("account_book:deleted_account_book_restore_or_hard_delete", kwargs={"pk": account_book.id})

    access_token, refresh_token = login
    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}

    response = client.patch(url, **headers)

    data = json.loads(response.content)

    assert response.status_code == 404
    assert data["detail"] == "찾을 수 없습니다."
