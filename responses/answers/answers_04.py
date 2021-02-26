import requests
import responses
import pytest
import json

from urllib.parse import urlparse

# Exercise 6.4
# Create a test data object test_data_zip
# with three lines / test cases:
# country code - zip code - place
#           us -    90210 - Beverly Hills
#           it -    50123 - Firenze
#           ca -      Y1A - Whitehorse
test_data_zip = [
    ("us", "90210", "Beverly Hills"),
    ("it", "50123", "Firenze"),
    ("ca", "Y1A", "Whitehorse"),
]


# Exercise 6.5
# Create a mock that uses a callback to create dynamic responses
# Upon receiving a GET call to http://api.zippopotam.us/<country_code>/<zip_code>
#   it should return a status code 200 and a JSON response body like this:
#   {'value': '<country_code> zip code <zip_code> corresponds to <place>'}
# Create a parameterized test (see Exercise 2.2 from the requests exercises) that takes three
#   arguments: country_code and zip_code as input parameters and place as
#   expected output. Perform a GET call to http://api.zippopotam.us/<country_code>/<zip_code>
#   and check that the response body element 'value' has a value equal to
#   '<country_code> zip code <zip_code> corresponds to <place>'.
@pytest.mark.parametrize("country_code, zip_code, place", test_data_zip)
@responses.activate
def test_using_a_callback_for_dynamic_responses(country_code, zip_code, place):
    def request_callback(request):
        request_url = request.url
        resp_body = {"value": generate_response_from(request_url)}
        return 200, {}, json.dumps(resp_body)

    responses.add_callback(
        responses.GET,
        f"http://api.zippopotam.us/{country_code}/{zip_code}",
        callback=request_callback,
        content_type="application/json",
    )

    def generate_response_from(url):
        parsed_url = urlparse(url).path
        split_url = parsed_url.split("/")
        return f"{split_url[-2]} zip code {split_url[-1]} corresponds to {place}"

    response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
    assert (
        response.json()["value"]
        == f"{country_code} zip code {zip_code} corresponds to {place}"
    )
