import os
import pickle


def save_data(data, filename):
    directory = os.path.dirname(filename)

    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(filename, "wb") as file:
        pickle.dump(data, file)


def load_data(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)