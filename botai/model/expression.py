class Expression(object):
    def __init__(self, text, doc, entities):
        self.text = text
        self.doc = doc
        self.entities = entities

    def intent(self):
        return next((entity for entity in self.entities if entity.type == 'intent'), None)
