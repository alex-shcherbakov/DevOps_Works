from JsonReader import JsonReader
from CsvToJsonConverter import CsvToJsonConverter

if __name__ == "__main__":
    csv_url = "https://informer.com.ua/dut/python/import/st_gt.csv"
    json_path = "students_data.json"  # Шлях до файлу JSON

    # Ініціалізація CsvToJsonConverter та виконання конвертації
    converter = CsvToJsonConverter()
    converter.read_and_convert(csv_url, json_path)

    # Читання та відображення даних з JSON
    json_reader = JsonReader()
    json_reader.display_data(json_path)
