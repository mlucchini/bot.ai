class Expression(object):
    def __init__(self, text, entities):
        self.text = text
        self.entities = entities

    def intent(self):
        return next((entity for entity in self.entities if entity.type == 'intent'), None)
