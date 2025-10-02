import re
from datetime import date
from typing import Optional

class Student:
    # приватні поля
    def __init__(self, full_name: str, group_number: str, birth_date: Optional[date] = None, address: Optional[str] = None):

        self.full_name = full_name
        self.group_number = group_number
        self.birth_date = birth_date
        self.address = address

    # Гетери + Сетери
    @property
    def full_name(self) -> str:
        return self._full_name

    @full_name.setter
    def full_name(self, value: str):
        if not value or not isinstance(value, str) or not re.match(r"^[А-Яа-яІіЄєЇї\s']+$", value):
            raise ValueError("ПІБ повинно бути непорожнім рядком, що містить лише літери та пробіли.")
        self._full_name = value.strip()

    @property
    def group_number(self) -> str:
        return self._group_number

    @group_number.setter
    def group_number(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("Номер групи повинен бути непорожнім рядком.")
        self._group_number = value.strip().upper()

    @property
    def birth_date(self) -> Optional[date]:
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value: Optional[date]):
        if value is not None:
            if not isinstance(value, date):
                raise TypeError("Дата народження повинна бути об'єктом datetime.date.")
            if value > date.today():
                raise ValueError("Дата народження не може бути в майбутньому.")
        self._birth_date = value

    @property
    def address(self) -> Optional[str]:
        return self._address

    @address.setter
    def address(self, value: Optional[str]):
        if value is not None and not isinstance(value, str):
            raise TypeError("Адреса повинна бути рядком або None.")
        self._address = value.strip() if value else None

    # додатковий метод для зручного представлення
    def __str__(self) -> str:
        info = (
            f"Студент: {self.full_name}, Група: {self.group_number}"
        )
        if self.birth_date:
            info += f", Дата народження: {self.birth_date.isoformat()}"
        if self.address:
            info += f", Адреса: {self.address}"
        return info

    def __repr__(self) -> str:
        return (
            f"Student(full_name='{self.full_name}', group_number='{self.group_number}', "
            f"birth_date={repr(self.birth_date)}, address={repr(self.address)})"
        )