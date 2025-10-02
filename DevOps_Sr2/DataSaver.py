from abc import ABC, abstractmethod
from typing import Dict, Any
from StudentData import StudentData


class DataSaver(ABC):
    def __init__(self, data_aggregator: StudentData, filename_parts: Dict[str, str]):
        self._data_aggregator = data_aggregator
        self._filename_parts = filename_parts

        self._data_to_save = self._data_aggregator.to_dict()

    @property
    def data_to_save(self) -> Dict[str, Any]:
        return self._data_to_save

    @staticmethod
    def _sanitize_name(name: str) -> str:
        return name.split()[0].replace('-', '').replace('\'', '')

    def _generate_filename(self, file_extension: str) -> str:
        pib_part = self._sanitize_name(self._filename_parts["ПІБ"])
        group_part = self._filename_parts["ГРУПА"]
        work_num_part = self._filename_parts["НОМЕР-РОБОТИ"]

        return f"{pib_part}_{group_part}_{work_num_part}.{file_extension.upper()}"

    @abstractmethod
    def save(self) -> str:
        pass