import requests


def test_get_user_with_id_1_check_status_code_equals_200():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200


def test_get_user_with_id_1_check_content_type_equals_json():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"


def test_get_user_with_id_1_check_encoding_equals_utf8():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.encoding == "utf-8"


def test_get_user_with_id_1_check_name_equals_leanne_graham():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    response_body = response.json()
    assert response_body["name"] == "Leanne Graham"


def test_get_user_with_id_1_check_company_name_equals_romaguera_crona():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    response_body = response.json()
    assert response_body["company"]["name"] == "Romaguera-Crona"


def test_get_all_users_check_number_of_users_equals_10():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    response_body = response.json()
    assert len(response_body) == 10


def test_get_user_with_id_1_check_full_body_response():

    expected_response_body = {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
        }
    }

    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    actual_response_body = response.json()
    assert expected_response_body == actual_response_body
