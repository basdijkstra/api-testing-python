import requests
import requests_mock


def test_requests_mock_hello_world():

    with requests_mock.Mocker() as mock:

        mock.get("https://api.helloworld.com",
                 status_code=200,
                 json={"message": "Hello, world!"})

        response = requests.get("https://api.helloworld.com")

        assert response.status_code == 200
        assert response.json()["message"] == "Hello, world!"
