from blockext import run, reporter, command, predicate
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np


class Model:
    def __init__(self):
        self.x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        self.y = np.array([0, 1, 1, 0])
        self.is_busy = False
        self.score = [0, 0]


    def build(self):
        self.model = Sequential()
        self.model.add(Dense(2, input_dim=2))
        self.model.add(Activation('sigmoid'))
        self.model.add(Dense(1))
        self.model.add(Activation('sigmoid'))


    def train(self):
        self.model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
        self.model.fit(self.x, self.y, epochs=10000)
        self.score = self.model.evaluate(self.x, self.y)


@command("start training")
def train():
    model.is_busy = True
    model.build()
    model.train()
    model.is_busy = False


@predicate("is busy")
def is_busy():
    return model.is_busy


@reporter("get score")
def get_score():
    return "%d" % (model.score[1] * 100)


if __name__ == "__main__":
    model = Model()
    run("XOR", "xor", 5678)
