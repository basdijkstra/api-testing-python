import requests
import responses
import pytest


# Exercise 3.1
# Write a test that does the following:
# Create a mock that returns an HTTP status code 200
#   for a GET request to http://api.zippopotam.us/us/90210
# Perform a GET  to http://api.zippopotam.us/us/90210
# Check that the number of calls made to the mock is equal to 1
@responses.activate
def test_get_data_for_us_90210_invokes_mock_exactly_once():

    responses.add(responses.GET, "http://api.zippopotam.us/us/90210", status=200)

    requests.get("http://api.zippopotam.us/us/90210")
    assert len(responses.calls) == 1


# Exercise 3.2
# Write a test that does the following:
# Create a mock that returns an HTTP status code 200
#   for a GET request to http://api.zippopotam.us/us/90210
# Perform a GET to http://api.zippopotam.us/us/90210
# Check that the first request received was to http://api.zippopotam.us/us/90210
@responses.activate
def test_get_data_for_us_90210_first_request_received_contains_expected_url():

    responses.add(responses.GET, "http://api.zippopotam.us/us/90210", status=200)

    requests.get("http://api.zippopotam.us/us/90210")
    assert responses.calls[0].request.url == "http://api.zippopotam.us/us/90210"


# Exercise 3.3
# Write a test that does the following:
# Create a mock that returns an HTTP status code 201
#   for a POST request to http://api.zippopotam.us/us/90210
# Perform a POST to http://api.zippopotam.us/us/90210
#   with request body {"data": "New location data for US zip code 90210"}
# Check that the response body of the first request received equals
#   '{"data": "New location data for US zip code 90210"}'
# Hint: the request body is stored in request.body in the byte data format,
# use the .decode('utf-8') function to make your assertion easier.
@responses.activate
def test_post_data_for_us_90210_first_request_received_contains_expected_data():

    responses.add(responses.POST, "http://api.zippopotam.us/us/90210", status=201)

    requests.post(
        "http://api.zippopotam.us/us/90210",
        json={"data": "New location data for US zip code 90210"}
    )

    assert responses.calls[0].request.body.decode('utf-8') == '{"data": "New location data for US zip code 90210"}'
