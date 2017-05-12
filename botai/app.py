from flask import Flask, request, Response

from botai.service import entities, expressions, metadata
from botai.util.converter import to_json

app = Flask(__name__)


@app.route('/entities', methods=['GET'])
def entities_api():
    text = request.args.get('text')
    return json(entities.get(text))


@app.route('/expressions', methods=['GET'])
def expressions_api():
    return json(expressions.get())


@app.route('/metadata', methods=['GET'])
def metadata_api():
    return json(metadata.get())


def json(obj):
    return Response(to_json(obj), mimetype='application/json')
