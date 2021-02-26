import requests
import responses
import pytest
import json

from urllib.parse import urlparse

test_data = [1, 2, 3]


@pytest.mark.parametrize('userid', test_data)
@responses.activate
def test_using_a_callback_for_dynamic_responses(userid):

    def request_callback(request):
        resp_body = {"value": generate_response_from(request.url)}
        return 200, {}, json.dumps(resp_body)

    responses.add_callback(
        responses.GET,
        f"https://jsonplaceholder.typicode.com/users/{userid}",
        callback=request_callback,
        content_type="application/json"
    )

    def generate_response_from(url):
        parsed_url = urlparse(url).path
        split_url = parsed_url.split('/')
        return f'You requested data for user {split_url[-1]}'

    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{userid}')
    assert response.json()["value"] == f"You requested data for user {userid}"
