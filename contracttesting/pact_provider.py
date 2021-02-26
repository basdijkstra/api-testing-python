import uuid

from flask import jsonify, request

from contracttesting.src.provider import app, fakedb


@app.route('/_pact/provider_states', methods=['POST'])
def provider_states():
    mapping = {'Location does not exist in database': setup_no_location_data,
               'Location exists in database': setup_location_data,
               'Requested zip code is invalid': setup_no_location_data}
    mapping[request.json['state']]()
    return jsonify({'result': request.json['state']})


def setup_no_location_data():
    if '90210' in fakedb:
        del fakedb['90210']


def setup_location_data():

    location_id = uuid.uuid4()

    fakedb['90210'] = {
        'id': location_id,
        'zip_code': '90210',
        'country': 'United States',
        'place_name': 'Beverly Hills',
        'state': 'California',
        'active': True
    }


if __name__ == '__main__':
    app.run(debug=True, port=9876)
