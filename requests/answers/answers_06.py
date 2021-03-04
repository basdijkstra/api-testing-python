import requests


# Exercise 6.1
# Using https://api.spacex.land/graphql/, build a GraphQL query
# that retrieves the 'ceo' of the 'company'. Write a test that POSTs
# this query to https://api.spacex.land/graphql/ and assert that
# the response status code is equal to 200
query_company_ceo = """
{
  company {
    ceo
    name
  }
}
"""


def test_retrieve_company_ceo_should_yield_http_200():
    response = requests.post("https://api.spacex.land/graphql/", json={'query': query_company_ceo})
    print(response.headers)
    assert response.status_code == 200


# Exercise 6.2
# Using the same POST request, assert that the value of the
# response header 'Server' is equal to 'Cowboy'
def test_retrieve_company_ceo_should_yield_server_cowboy():
    response = requests.post("https://api.spacex.land/graphql/", json={'query': query_company_ceo})
    assert response.headers['Server'] == 'Cowboy'


# Exercise 6.3
# Using the same POST request, assert that the value of the
# response encoding is equal to 'utf-8'
def test_retrieve_company_ceo_should_yield_encoding_utf8():
    response = requests.post("https://api.spacex.land/graphql/", json={'query': query_company_ceo})
    assert response.encoding == 'utf-8'


# Exercise 6.4
# Using the same POST request, assert that the value of the
# response body element 'ceo' (data > company > ceo) is 'Elon Musk'
def test_retrieve_company_ceo_should_yield_ceo_elon_musk():
    response = requests.post("https://api.spacex.land/graphql/", json={'query': query_company_ceo})
    response_body = response.json()
    assert response_body['data']['company']['ceo'] == 'Elon Musk'


# Exercise 6.5
# Using https://api.spacex.land/graphql/, build a GraphQL query
# that retrieves the 'id' for all 'missions'.
# Write a test that POSTs this query to https://api.spacex.land/graphql/
# and assert that the response status code is equal to 200
query_missions = """
{
  missions {
    id
  }
}
"""


def test_retrieve_mission_ids_count_should_be_10():
    response = requests.post("https://api.spacex.land/graphql/", json={'query': query_missions})

    response_body = response.json()
    assert len(response_body['data']['missions']) == 10
