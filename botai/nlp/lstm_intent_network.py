import logging
import operator

import numpy as np
from keras.layers import LSTM, Dropout, Dense
from keras.models import Sequential
from keras.utils import np_utils
from sklearn.model_selection import train_test_split

from botai.model.expression import Expression
from botai.model.intent import Intent

LSTM_OUTPUT_SPACE = 128
BATCH_SIZE = 64
EPOCHS = 10
DOCUMENT_MAX_NUM_WORDS = 50

logging.getLogger('tensorflow').disabled = True


class LSTMIntentNetwork(object):
    def __init__(self, nlp, expressions):
        self.nlp = nlp
        self.all_expressions = expressions
        self.num_features = nlp.vocab.vectors_length
        self.categories = list(set([expression.intent().name for expression in expressions]))

        intents = [expression.intent().name for expression in expressions]
        intents_indices = [self.categories.index(intent) for intent in intents]

        self.x = np.zeros(shape=(len(expressions), DOCUMENT_MAX_NUM_WORDS, self.num_features)).astype('float32')
        self.__init_x(self.x, expressions)

        self.y = np_utils.to_categorical(intents_indices)

        self.model = Sequential()
        self.model.add(LSTM(int(DOCUMENT_MAX_NUM_WORDS * 1.5), input_shape=(DOCUMENT_MAX_NUM_WORDS, self.num_features)))
        self.model.add(Dropout(0.3))
        self.model.add(Dense(len(self.categories), activation='sigmoid'))
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    def train(self):
        x_train, x_test, y_train, y_test = train_test_split(self.x, self.y, test_size=0.2)
        self.model.fit(x_train, y_train, batch_size=BATCH_SIZE, epochs=EPOCHS, validation_data=(x_test, y_test))
        score, acc = self.model.evaluate(x_test, y_test, batch_size=BATCH_SIZE)

        print('Score: %1.4f' % score)
        print('Accuracy: %1.4f' % acc)

    def predict(self, text):
        expressions = [Expression(text, None, [])]
        x = np.zeros(shape=(1, DOCUMENT_MAX_NUM_WORDS, self.num_features)).astype('float32')
        self.__init_x(x, expressions)
        predictions = self.model.predict(x)
        max_index, max_score = max(enumerate(predictions), key=operator.itemgetter(1))
        intent = self.categories[max_index]
        print('Predictions for "%s":' % text, zip(self.categories, predictions))
        return [Intent(text, intent, max_score, '')]

    def __init_x(self, x, expressions):
        documents = [self.nlp(expression.text) for expression in expressions]
        for idx, document in enumerate(documents):
            for jdx, word in enumerate(document):
                if jdx == DOCUMENT_MAX_NUM_WORDS:
                    break
                x[idx, jdx, :] = word.vector
