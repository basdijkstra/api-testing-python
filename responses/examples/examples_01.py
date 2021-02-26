import requests
import responses
import pytest

from requests.exceptions import ConnectionError


@responses.activate
def test_get_user_with_id_1_mock_returns_404():

    responses.add(
        responses.GET, "https://jsonplaceholder.typicode.com/users/1", status=404
    )

    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 404


@responses.activate
def test_get_user_with_id_1_mock_returns_404_and_error_message_in_body():

    responses.add(
        responses.GET,
        "https://jsonplaceholder.typicode.com/users/1",
        json={"error": "No data exists for user with ID 1"},
        status=404,
    )

    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.json()["error"] == "No data exists for user with ID 1"


@responses.activate
def test_unmatched_endpoint_raises_connectionerror():

    with pytest.raises(ConnectionError):
        requests.get("https://jsonplaceholder.typicode.com/users/99")
