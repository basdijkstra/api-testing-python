"""pact test for location service client"""

import logging
import os

from pact import Verifier

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


PACT_UPLOAD_URL = (
    "http://127.0.0.1/pacts/provider/UserService/consumer"
    "/Location_ServiceClient/version"
)
PACT_FILE = "locationserviceclient-locationservice.json"
PACT_BROKER_URL = "http://localhost"
PACT_BROKER_USERNAME = "pactbroker"
PACT_BROKER_PASSWORD = "pactbroker"

PACT_MOCK_HOST = 'localhost'
PACT_MOCK_PORT = 9876
PACT_URL = "http://{}:{}".format(PACT_MOCK_HOST, PACT_MOCK_PORT)
PACT_DIR = os.path.dirname(os.path.realpath(__file__))


def test_get_location():
    verifier = Verifier(provider='LocationService',
                        provider_base_url=PACT_URL)

    output, logs = verifier.verify_pacts(os.path.join(PACT_DIR, PACT_FILE),
                                         verbose=False,
                                         provider_states_setup_url="{}/_pact/provider_states".format(PACT_URL))

    assert (output == 0)
