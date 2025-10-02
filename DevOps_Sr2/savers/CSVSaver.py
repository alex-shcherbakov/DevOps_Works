import csv
import os
from DevOps_Sr2.model.StudentData import StudentData
from DevOps_Sr2.savers.DataSaver import DataSaver
from typing import Dict, Any, List


class CSVSaver(DataSaver):
    def __init__(self, data_aggregator: StudentData, filename_parts: Dict[str, str]):
        super().__init__(data_aggregator, filename_parts)

    def _prepare_csv_data(self) -> List[Dict[str, Any]]:
        data = self._data_to_save
        student_info = data["Студент"]
        real_performance = data["Реальна_успішність"]
        desired_performance = data["Бажана_успішність"]

        csv_rows = []

        subjects_details = [
            (real["Предмет"], real["Бал"], desired["Бажаний_бал"])
            for real, desired in zip(real_performance["Список_оцінок"], desired_performance["Список_бажаних_оцінок"])
        ]

        for subject, real_score, desired_score in subjects_details:
            row = {
                "ПІБ": student_info["ПІБ"],
                "Група": student_info["Група"],
                "Дата_народження": student_info["Дата_народження"],
                "Середній_бал_факт": real_performance["Середній_бал_фактичний"],
                "Середній_бал_бажаний": desired_performance["Бажаний_середній_бал"],
                "Предмет": subject,
                "Бал_фактичний": real_score,
                "Бал_бажаний": desired_score,
            }
            csv_rows.append(row)

        return csv_rows

    def save(self) -> str:
        filename = self._generate_filename("csv")
        csv_data = self._prepare_csv_data()

        if not csv_data:
            raise ValueError("Немає даних для запису у файл CSV.")

        fieldnames = list(csv_data[0].keys())

        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

                writer.writeheader()
                writer.writerows(csv_data)

            return os.path.abspath(filename)
        except IOError as e:
            raise IOError(f"Помилка при записі у файл CSV {filename}: {e}")