from botai.model.pos_entity import PosEntity


class PosEntityExtractor:
    def __init__(self, doc):
        self.entities = [PosEntity(entity.text, entity.start_char, entity.end_char, entity.label_.lower())
                         for entity in doc.ents]
