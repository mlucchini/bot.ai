from botai.model.entity import Entity


class Intent(Entity):
    def __init__(self, text, name, score=None, closest_match=None):
        self.text = text
        self.type = "intent"
        self.name = name
        self.score = score
        self.closest_match = closest_match
