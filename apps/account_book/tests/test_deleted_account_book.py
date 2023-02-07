import json

from rest_framework.reverse import reverse


def test_deleted_account_book_list_read_success(client, deleted_account_book, login):
    url = reverse("account_book:deleted_account_book")

    access_token, refresh_token = login
    headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}

    response = client.get(url, **headers)

    data = json.loads(response.content)

    assert response.status_code == 200
    assert data[0]["title"] == "test_title_deleted"
    assert data[0]["balance"] == 0
    assert data[0]["is_active"] == False
