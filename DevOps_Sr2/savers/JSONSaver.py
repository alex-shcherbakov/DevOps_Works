import json
import os
from DevOps_Sr2.model.StudentData import StudentData
from DevOps_Sr2.savers.DataSaver import DataSaver
from typing import Dict


class JSONSaver(DataSaver):
    def __init__(self, data_aggregator: StudentData, filename_parts: Dict[str, str]):
        super().__init__(data_aggregator, filename_parts)

    def save(self) -> str:
        filename = self._generate_filename("json")

        data_for_json = self._data_to_save.copy()

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data_for_json, f, indent=4, ensure_ascii=False)

            return os.path.abspath(filename)
        except IOError as e:
            raise IOError(f"Помилка при записі у файл JSON {filename}: {e}")