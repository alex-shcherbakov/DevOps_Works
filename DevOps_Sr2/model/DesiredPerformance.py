from typing import List

from DevOps_Sr2.model.AcademicPerformance import AcademicPerformance


class DesiredPerformance(AcademicPerformance):
    def __init__(self, subjects: List[str], scores: List[int], desired_score: float):
        super().__init__(subjects, scores)

        self._desired_score = None

        self.desired_score = desired_score

    # --- Гетери + Сетери ---
    @property
    def desired_score(self) -> float:
        return self._desired_score

    @desired_score.setter
    def desired_score(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Бажаний середній бал має бути числом.")
        if not (0.0 <= value <= 100.0):
            raise ValueError("Бажаний середній бал має бути у діапазоні від 0.0 до 100.0.")
        self._desired_score = float(value)

    # реалізація абстрактного методу
    def average_score(self) -> float:
        return self._desired_score