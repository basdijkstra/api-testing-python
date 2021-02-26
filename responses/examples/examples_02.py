import requests
import responses
import pytest


@responses.activate
def test_get_user_with_id_1_mock_returns_404():

    responses.add(
        responses.GET, "https://jsonplaceholder.typicode.com/users/1", status=404
    )

    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 404


@responses.activate
def test_responses_can_raise_error_on_demand():

    responses.add(
        responses.GET,
        "https://jsonplaceholder.typicode.com/users/99",
        body=RuntimeError("A runtime error occurred"),
    )

    with pytest.raises(RuntimeError) as re:
        requests.get("https://jsonplaceholder.typicode.com/users/99")
    assert str(re.value) == "A runtime error occurred"
