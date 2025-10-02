from abc import ABC, abstractmethod
from typing import List


class AcademicPerformance(ABC):
    # приватні поля + гетери/сетери
    def __init__(self, subjects: List[str], scores: List[int]):
        self._subjects = self._validate_subjects(subjects)
        self._scores = self._validate_scores(scores, self._subjects)

    @property
    def subjects(self) -> List[str]:
        return self._subjects

    @subjects.setter
    def subjects(self, value: List[str]):
        self._subjects = self._validate_subjects(value)

    @property
    def scores(self) -> List[int]:
        return self._scores

    @scores.setter
    def scores(self, value: List[int]):
        self._scores = self._validate_scores(value, self._subjects)

    def _validate_subjects(self, value: List[str]) -> List[str]:
        if not isinstance(value, list) or not all(isinstance(s, str) and s.strip() for s in value):
            raise TypeError("Список предметів має бути списком непорожніх рядків.")
        return [s.strip() for s in value]

    def _validate_scores(self, value: List[int], subjects: List[str]) -> List[int]:
        if not isinstance(value, list) or not all(isinstance(s, int) and 0 <= s <= 100 for s in value):
            raise TypeError("Список балів має бути списком цілих чисел у діапазоні від 0 до 100.")
        if len(subjects) != len(value):
            raise ValueError("Кількість балів повинна відповідати кількості предметів.")
        return value

    @abstractmethod
    def average_score(self) -> float:
        pass

    # додаткові методи для зручності
    def __str__(self) -> str:
        return f"Успішність по {len(self._subjects)} предметам."

    def get_performance_details(self) -> List[str]:
        details = []
        for subject, score in zip(self._subjects, self._scores):
            details.append(f"{subject}: {score} балів")
        return details

## клас-нащадок
class AcademicPerformanceImpl(AcademicPerformance):

    def average_score(self) -> float:
        if not self._scores:
            return 0.0
        return sum(self._scores) / len(self._scores)