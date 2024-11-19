import json
import os

class DataStorage:
    def __init__(self, filename='data.json'):
        self.filename = filename

    def load_data(self):
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, 'r') as file:
            return json.load(file)

    def save_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def append_data(self, new_data):
        current_data = self.load_data()
        current_data.update(new_data)
        self.save_data(current_data)
