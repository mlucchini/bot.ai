import tempfile
from os import environ

from pathlib import Path

from botai.app import app
from botai.db.in_memory import InMemoryDb
from botai.nlp.english import English
from botai.nlp.entity_trainer import EntityTrainer

__version__ = (0, 0, 1)

if __name__ == '__main__':
    training_dir = Path(tempfile.gettempdir() + '/bot_ai_training_directory')

    english = English.instance()
    english.load()

    db = InMemoryDb.instance()
    db.load()

    trainer = EntityTrainer(english.nlp, training_dir)
    trainer.train(db.expressions)
    english.load(training_dir)

    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
