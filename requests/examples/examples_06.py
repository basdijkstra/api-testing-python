import requests

query_continents = """
{
  continents {
    name
  }
}
"""


def test_get_list_of_continents_first_one_should_be_africa():
    response = requests.post("https://countries.trevorblades.com/", json={'query': query_continents})
    assert response.status_code == 200
    response_body = response.json()
    assert response_body['data']['continents'][0]['name'] == 'Africa'

