
#!/usr/bin/env python3

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping
from preprocessing import encode_data, oversample, scale_features, select_features, split_data, df
from joblib import dump
import os



def create_model(input_shape, dense_units, n_dense_layers=1, activation='relu', output_activation='sigmoid', learning_rate=0.001):
    model = Sequential()

    for _ in range(n_dense_layers):
        model.add(Dense(dense_units, input_shape=input_shape, activation=activation))

    model.add(Dense(1, activation=output_activation))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    return model

def prepare_data(df):
    df_encoded = encode_data(df)
    X = df_encoded.drop('y', axis=1)
    Y = df_encoded['y']
    Y = Y.astype(int)
    X_selected = select_features(X, Y, missing_threshold=0.5)
    print(X_selected)
    X_resampled, Y_oversampled = oversample(X_selected, Y)
    print(X_resampled)
    X_scaled = scale_features(X_resampled)
    x_train, x_test, x_val, y_train, y_test, y_val = split_data(X_scaled, Y_oversampled)
    return x_train, y_train, x_val, y_val

def train_and_save_model(x_train, y_train, x_val, y_val):
    model = create_model(input_shape=(x_train.shape[1],), dense_units=10, n_dense_layers=3)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_val, y_val))
    _, accuracy = model.evaluate(x_val, y_val)
    print(f'Model Accuracy: {accuracy * 100:.2f}%')

    try:
        print("Current working directory:", os.getcwd())
        if not os.path.exists('models'):
            os.makedirs('models')
        dump(model, '../models/model.joblib')
        print("Model saved successfully.")
    except Exception as e:
        print("Error saving model:", str(e))
# Use the functions
x_train, y_train, x_val, y_val = prepare_data(df)
train_and_save_model(x_train, y_train, x_val, y_val)
