"""Описываем модель сотрудники"""


class Employee:
    def __init__(self, id_: int, employee_full_name: str, in_work, out_work, bonus_code: list, base_salary: int):
        self.base_salary = base_salary
        self.bonus_code = bonus_code
        self.out_work = out_work
        self.in_work = in_work
        self.employee_full_name = employee_full_name
        self.id_ = id_
