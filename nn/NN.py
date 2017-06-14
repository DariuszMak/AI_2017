import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import numpy as np

class NN:
    def __init__(self):
        self.model = keras.models.load_model("./model")

    def getPackageDecision(self, grid, package, x, y, targets, dt):
        return self.model.predict(np.asarray([x, y]).reshape(2))
