import json

from botai.model.expression import Expression
from botai.model.intent import Intent
from botai.model.pos_entity import PosEntity
from botai.util.converter import to_json

expressions_filename = 'expressions.json'


class JsonLoader(object):
    def __init__(self, folder):
        self.folder = folder

    def expressions(self):
        try:
            text = self.__to_string(expressions_filename)
            elements = json.loads(text)['data']
            return [self.expression(element) for element in elements]
        except ValueError, e:
            print('Invalid expressions JSON. %s' % e)

    def expression(self, element):
        text = element['text']
        entities = []
        for entity in element['entities']:
            name = entity['entity']
            value = entity['value']
            if name == 'intent':
                entities.append(Intent(text, value))
            else:
                entities.append(PosEntity(value, entity['start'], entity['end'], name))
        return Expression(text, entities)

    def __to_string(self, filename):
        path = self.folder + '/' + filename
        with open(path, 'r') as f:
            return f.read()


if __name__ == '__main__':
    loader = JsonLoader('data')
    print(to_json(loader.expressions()))
