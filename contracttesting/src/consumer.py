import requests


class LocationConsumer(object):
    def __init__(self, base_uri):
        self.base_uri = base_uri

    def get_location(self, zip_code):
        """Fetch a user object by zip code from the server."""
        uri = f'{self.base_uri}/{zip_code}'
        response = requests.get(uri)
        if response.status_code in (400, 404):
            return None

        place_name = response.json()['place_name']
        return Location(place_name)


class Location(object):
    def __init__(self, place_name):
        self.place_name = place_name
