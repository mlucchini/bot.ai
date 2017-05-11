from flask import Flask, request, Response

from service import entities
from service import expressions
from util.converter import to_json

app = Flask(__name__)


@app.route('/entities')
def entities_api():
    text = request.args.get('text')
    return json(entities.get(text))


@app.route('/expressions')
def expressions_api():
    return json(expressions.get())


def json(obj):
    return Response(to_json(obj), mimetype='application/json')
