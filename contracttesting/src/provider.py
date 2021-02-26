from flask import Flask, abort, jsonify

fakedb = {}

app = Flask(__name__)


@app.route('/<zip_code>')
def get_location_by_zip(zip_code):
    location_data = fakedb.get(zip_code)
    if not location_data:
        abort(404)
    response = jsonify(**location_data)
    app.logger.debug('GET location for %s returns data:\n%s', zip_code, response.data)
    return response


if __name__ == '__main__':
    app.run(debug=True, port=5001)
