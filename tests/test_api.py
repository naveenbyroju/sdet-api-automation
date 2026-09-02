from api.api_client import APIClient


def test_get_posts():
    api_client = APIClient()

    response = api_client.get("/posts/1")

    assert response.status_code == 200

    response_body = response.json()

    assert response_body["id"] == 1
    assert "title" in response_body
    assert "body" in response_body


def test_create_post():
    api_client = APIClient()

    payload = {
        "title": "SDET API Automation",
        "body": "Testing POST API using Pytest and Requests",
        "userId": 1
    }

    response = api_client.post("/posts", payload)

    assert response.status_code == 201

    response_body = response.json()

    assert response_body["title"] == payload["title"]
    assert response_body["body"] == payload["body"]
    assert response_body["userId"] == payload["userId"]