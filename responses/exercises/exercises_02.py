import requests
import responses
import pytest


# Exercise 2.1
# Write a test that does the following:
# Create a mock that returns an HTTP status code 405
#   for a DELETE request to http://api.zippopotam.us/us/90210
# Perform a DELETE to http://api.zippopotam.us/us/90210
# Check that the status code is indeed equal to 405
@responses.activate
def test_delete_data_for_us_90210_mock_returns_405():

    pass


# Exercise 2.2
# Write a test that does the following:
# Create a mock that raises a ValueError
#   for a GET request to http://api.zippopotam.us/us/ABCDE
#   with a message 'US uses numerical zip codes only'
# Perform a GET to http://api.zippopotam.us/us/ABCDE
# Check that a ValueError is raised indeed and that the
#   associated message equals 'US uses numerical zip codes only'
# An example of how to do that can be found at
#   https://pybit.es/guest-pytest-raises.html
@responses.activate
def test_responses_can_raise_error_on_demand():

    pass
