import requests
import responses


# Exercise 1.1
# Write a test that does the following:
# Create a mock that returns an HTTP status code 201
#   for a POST request to http://api.zippopotam.us/us/90210
# Perform a POST to http://api.zippopotam.us/us/90210
# Check that the status code is indeed equal to 201
@responses.activate
def test_post_data_for_us_90210_mock_returns_201():

    pass


# Exercise 1.2
# Write a test that does the following:
# Create a mock that returns an HTTP status code 200
#   for a GET request to http://api.zippopotam.us/us/90210
#   as well as a header 'Server' with value 'Served by responses mock'
# Perform a GET to http://api.zippopotam.us/us/90210
# Check that the value of the 'Server' response header
# is indeed equal to 'Served by responses mock'
@responses.activate
def test_get_data_for_us_90210_mock_returns_200_and_header():

    pass


# Exercise 1.3
# Write a test that does the following:
# Create a mock that returns an HTTP status code 200
#   for a GET request to http://api.zippopotam.us/lv/1050
#   as well as a JSON response body that looks like this:
#   {'data': 'LV zip code 1050 corresponds to Riga'}
# Perform a GET to http://api.zippopotam.us/lv/1050
# Check that the value of the 'data' element in the JSON
# response is indeed equal to 'LV zip code 1050 corresponds to Riga'
@responses.activate
def test_get_data_for_lv_1050_mock_returns_200_and_data_in_body():

    pass
