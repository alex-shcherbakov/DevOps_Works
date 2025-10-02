from DevOps_Sr2.model.Student import Student
from DevOps_Sr2.model.AcademicPerformance import AcademicPerformanceImpl
from DevOps_Sr2.model.DesiredPerformance import DesiredPerformance
from typing import Dict, Any


class StudentData:
    def __init__(self, student: Student, real_performance: AcademicPerformanceImpl,
                 desired_performance: DesiredPerformance):
        # приватні поля
        self._student = student
        self._real_performance = real_performance
        self._desired_performance = desired_performance

        # перевірка списків предметів
        if self._real_performance.subjects != self._desired_performance.subjects:
            raise ValueError("Списки предметів для реальної та бажаної успішності повинні збігатися.")

    @property
    def student(self) -> Student:
        return self._student

    @property
    def real_performance(self) -> AcademicPerformanceImpl:
        return self._real_performance

    @property
    def desired_performance(self) -> DesiredPerformance:
        return self._desired_performance

    # головний метод агрегації
    def to_dict(self) -> Dict[str, Any]:
        student_data = {
            "ПІБ": self._student.full_name,
            "Група": self._student.group_number,
            "Дата_народження": self._student.birth_date.isoformat() if self._student.birth_date else None,
            "Адреса": self._student.address
        }

        real_performance_details = [
            {"Предмет": sub, "Бал": score}
            for sub, score in zip(self._real_performance.subjects, self._real_performance.scores)
        ]

        real_performance_data = {
            "Список_оцінок": real_performance_details,
            "Середній_бал_фактичний": self._real_performance.average_score()
        }

        desired_performance_details = [
            {"Предмет": sub, "Бажаний_бал": score}
            for sub, score in zip(self._desired_performance.subjects, self._desired_performance.scores)
        ]

        desired_performance_data = {
            "Список_бажаних_оцінок": desired_performance_details,
            "Бажаний_середній_бал": self._desired_performance.average_score()
        }

        final_dict = {
            "Студент": student_data,
            "Реальна_успішність": real_performance_data,
            "Бажана_успішність": desired_performance_data
        }
        return final_dict