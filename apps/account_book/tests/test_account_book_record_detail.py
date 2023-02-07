import json

from rest_framework.reverse import reverse


def test_account_book_record_read_success(client, account_book, account_book_record, login):
    url = reverse(
        "account_book:account_book_record_detail", kwargs={"pk": account_book.id, "record_pk": account_book_record.id}
    )
    access_token, refresh_token = login

    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}
    response = client.get(url, **headers)

    data = json.loads(response.content)

    assert response.status_code == 200
    assert data["account_book"] == account_book.id
    assert data["date"] == "2023-01-01"
    assert data["amount"] == 1
    assert data["description"] == "test_description"
    assert data["is_active"] == True


def test_account_book_record_read_fail_with_unauthorized_user(client, account_book, account_book_record, login_b):
    url = reverse(
        "account_book:account_book_record_detail", kwargs={"pk": account_book.id, "record_pk": account_book_record.id}
    )
    access_token, refresh_token = login_b

    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}
    response = client.get(url, **headers)

    data = json.loads(response.content)

    assert response.status_code == 403
    assert data["detail"] == "이 작업을 수행할 권한(permission)이 없습니다."


def test_account_book_record_update_success(client, account_book, account_book_record, login):
    url = reverse(
        "account_book:account_book_record_detail", kwargs={"pk": account_book.id, "record_pk": account_book_record.id}
    )
    access_token, refresh_token = login

    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}
    data = {"date": "1111-11-11", "amount": 111, "description": "test_description_update"}
    response = client.patch(url, data=data, content_type="application/json", **headers)

    data = json.loads(response.content)

    assert response.status_code == 200
    assert data["amount"] == 111
    assert data["description"] == "test_description_update"
    assert data["updated_at"]


def test_account_book_record_update_fail_with_no_data(client, account_book, account_book_record, login):
    url = reverse(
        "account_book:account_book_record_detail", kwargs={"pk": account_book.id, "record_pk": account_book_record.id}
    )
    access_token, refresh_token = login

    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}
    data = {
        # "date": "1111-11-11",
        # "amount": 111,
        # "description": "test_description_update"
    }
    response = client.patch(url, data=data, content_type="application/json", **headers)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["non_field_errors"][0] == "입력값이 없습니다."


def test_account_book_record_delete_success(client, account_book, account_book_record, login):
    url = reverse(
        "account_book:account_book_record_detail", kwargs={"pk": account_book.id, "record_pk": account_book_record.id}
    )
    access_token, refresh_token = login

    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}

    response = client.delete(url, **headers)

    data = json.loads(response.content)

    assert response.status_code == 200
    assert data["is_active"] == False
    assert data["deleted_at"]


def test_account_book_record_delete_fail_with_deleted_account_book_record(
    client, account_book, deleted_account_book_record, login
):
    url = reverse(
        "account_book:account_book_record_detail",
        kwargs={"pk": account_book.id, "record_pk": deleted_account_book_record.id},
    )
    access_token, refresh_token = login

    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}

    response = client.delete(url, **headers)

    assert response.status_code == 404
