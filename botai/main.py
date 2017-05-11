from os import environ

from botai.app import app
from botai.db.in_memory import InMemoryDb
from botai.nlp.english import English
from botai.nlp.entity_trainer import EntityTrainer

__version__ = (0, 0, 1)

if __name__ == '__main__':
    English.instance()
    InMemoryDb.instance()
    EntityTrainer().train(InMemoryDb.instance().expressions)

    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
