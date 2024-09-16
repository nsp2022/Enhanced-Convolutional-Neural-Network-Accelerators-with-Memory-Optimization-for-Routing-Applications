from save_load import *
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dropout, Dense, MaxPooling2D
from tensorflow.keras.datasets import mnist
import numpy as np

from keras import regularizers
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
import numpy as np

X_train =load("x_train")
X_test = load("x_test")
y_test = load("y_test")
y_train = load("y_train")

# Assuming you have X_train, X_test, y_train, y_test from the previous example
# If not, replace them with your actual data

def cnn_accelarator(X_train,Y_train,X_test,Y_test):

    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(X_train[1].shape)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))

    # Flatten the output before the dense layers
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1, activation='softmax'))

    # Compile the model
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    # Normalize pixel values to be between 0 and 1
    X_train_normalized = X_train / 255.0
    X_test_normalized = X_test / 255.0

    # Train the model
    model.fit(X_train_normalized, y_train, epochs=10, validation_data=(X_test_normalized, y_test))

    # Evaluate the model
    test_loss, test_acc = model.evaluate(X_test_normalized, y_test)
    print(f'Test accuracy: {test_acc}')

    # Make predictions
    predictions = model.predict(X_test_normalized)

    return predictions

