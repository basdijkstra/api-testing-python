import requests
import responses
import pytest
import json

from urllib.parse import urlparse
from requests.exceptions import ConnectionError


@responses.activate
def test_get_user_with_id_1_performs_exactly_1_call():

    responses.add(
        responses.GET, "https://jsonplaceholder.typicode.com/users/1", status=200
    )

    requests.get("https://jsonplaceholder.typicode.com/users/1")

    assert len(responses.calls) == 1


@responses.activate
def test_get_user_with_id_1_invokes_expected_url():

    responses.add(
        responses.GET, "https://jsonplaceholder.typicode.com/users/1", status=200
    )

    requests.get("https://jsonplaceholder.typicode.com/users/1")

    assert responses.calls[0].request.url == "https://jsonplaceholder.typicode.com/users/1"
