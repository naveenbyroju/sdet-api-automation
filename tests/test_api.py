import requests


def test_get_posts():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    assert response.status_code == 200

    response_body = response.json()

    assert response_body["id"] == 1
    assert "title" in response_body
    assert "body" in response_body