import json
from DataReader import DataReader

class JsonReader(DataReader):
    def read_data(self, path):
        """Читання даних з JSON файлу."""
        with open(path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data

    def display_data(self, path):
        """Читання та відображення даних з JSON файлу."""
        data = self.read_data(path)
        print("Дані прочитані з JSON файлу:")
        for row in data:
            print(row)
