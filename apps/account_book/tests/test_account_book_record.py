import json

from rest_framework.reverse import reverse


def test_account_book_record_create_success(client, account_book, login):
    url = reverse("account_book:account_book_record", kwargs={"pk": account_book.id})
    access_token, refresh_token = login

    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}
    data = {"date": "2023-01-01", "amount": 1, "description": "test_description"}
    response = client.post(url, data=data, **headers)

    data = json.loads(response.content)

    assert response.status_code == 201
    assert data["date"] == "2023-01-01"
    assert data["amount"] == 1
    assert data["description"] == "test_description"


def test_account_book_record_create_fail_with_no_data(client, account_book, login):
    url = reverse("account_book:account_book_record", kwargs={"pk": account_book.id})
    access_token, refresh_token = login

    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}
    data = {
        # "date": "2023-01-01",
        # "amount": 1,
        # "description": "test_description"
    }
    response = client.post(url, data=data, **headers)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["date"][0] == "이 필드는 필수 항목입니다."
    assert data["amount"][0] == "이 필드는 필수 항목입니다."
    assert data["description"][0] == "이 필드는 필수 항목입니다."


def test_account_book_record_create_fail_with_invalid_date_format(client, account_book, login):
    url = reverse("account_book:account_book_record", kwargs={"pk": account_book.id})
    access_token, refresh_token = login

    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}
    data = {"date": "20230101", "amount": 1, "description": "test_description"}
    response = client.post(url, data=data, **headers)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["date"][0] == "Date의 포멧이 잘못되었습니다. 이 형식들 중 한가지를 사용하세요: YYYY-MM-DD."


def test_account_book_record_create_fail_with_unauthorized_user(client, account_book, login_b):
    url = reverse("account_book:account_book_record", kwargs={"pk": account_book.id})
    access_token, refresh_token = login_b

    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}
    data = {"date": "2023-01-01", "amount": 1, "description": "test_description"}
    response = client.post(url, data=data, **headers)

    data = json.loads(response.content)

    assert response.status_code == 403
    assert data["detail"] == "이 작업을 수행할 권한(permission)이 없습니다."


def test_account_book_record_list_read_success(client, account_book, account_book_record, login):
    url = reverse("account_book:account_book_record", kwargs={"pk": account_book.id})
    access_token, refresh_token = login

    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}
    response = client.get(url, **headers)

    data = json.loads(response.content)

    assert response.status_code == 200

    assert data[0]["date"] == "2023-01-01"
    assert data[0]["amount"] == 1
    assert data[0]["description"] == "test_description"
    assert data[0]["is_active"] == True


def test_account_book_record_list_read_fail_with_unauthorized_user(client, account_book, account_book_record, login_b):
    url = reverse("account_book:account_book_record", kwargs={"pk": account_book.id})
    access_token, refresh_token = login_b

    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}
    response = client.get(url, **headers)

    data = json.loads(response.content)

    assert response.status_code == 403
    assert data["detail"] == "이 작업을 수행할 권한(permission)이 없습니다."
