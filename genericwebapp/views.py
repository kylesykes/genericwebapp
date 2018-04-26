# Flask creates an `app` object with the same name as the file this code is in.
# This is the main Flask object and what you always need to do for Flask programs.

import json

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/status', methods=['GET'])
@app.route('/', methods=['GET'])
def test_status():
    """
    Put in a status check here. 
    """
    return jsonify({
        "message": "Successful GET Test"
        })


if __name__ == '__main__':
    # When this file is run as a module (instead of imported as library) it will
    # run with the Python development webserver included in the core libraries.
    app.run('localhost', 8080, debug=True)
