from botai.model.entity import Entity


class PosEntity(Entity):
    def __init__(self, text, start, end, entity_type):
        self.text = text
        self.start = start
        self.end = end
        self.type = entity_type
