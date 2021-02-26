"""pact test for user service client"""

import logging
import os
import atexit

import pytest
from pact import Consumer, Like, Provider, Term, Format

from contracttesting.src.consumer import LocationConsumer

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
print(Format().__dict__)

PACT_BROKER_URL = "http://localhost"
PACT_FILE = "locationserviceclient-locationservice.json"
PACT_BROKER_USERNAME = "pactbroker"
PACT_BROKER_PASSWORD = "pactbroker"

PACT_MOCK_HOST = 'localhost'
PACT_MOCK_PORT = 1234
PACT_DIR = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
def consumer():
    return LocationConsumer(
        'http://{host}:{port}'
        .format(host=PACT_MOCK_HOST, port=PACT_MOCK_PORT)
    )


@pytest.fixture(scope='session')
def pact(request):
    version = request.config.getoption('--publish-pact')
    publish = True if version else False

    pact = Consumer('LocationServiceClient', version=version).has_pact_with(
        Provider('LocationService'), host_name=PACT_MOCK_HOST, port=PACT_MOCK_PORT,
        pact_dir=PACT_DIR, publish_to_broker=publish, broker_base_url=PACT_BROKER_URL,
        broker_username=PACT_BROKER_USERNAME, broker_password=PACT_BROKER_PASSWORD)

    print('start service')
    pact.start_service()
    atexit.register(pact.stop_service)

    yield pact
    print('stop service')
    pact.stop_service()


def test_get_existing_location(pact, consumer):
    expected = {
        'id': Format().uuid,
        'zip_code': '90210',
        'country': 'United States',
        'place_name': 'Beverly Hills',
        'state': 'California',
        'active': True
    }

    (pact
     .given('Location exists in database')
     .upon_receiving('a request for 90210')
     .with_request('get', '/90210')
     .will_respond_with(200, body=Like(expected)))

    with pact:
        location = consumer.get_location('90210')
        assert location.place_name == 'Beverly Hills'


def test_get_nonexisting_location(pact, consumer):
    (pact
     .given('Location does not exist in database')
     .upon_receiving('a request for 90210')
     .with_request('get', '/90210')
     .will_respond_with(404))

    with pact:
        location = consumer.get_location('90210')
        assert location is None
