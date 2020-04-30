from Logic.AppendDataToModel import AppendContracts, AppendEmployees

"""Списки сущностей"""


class LocalData:

    def __init__(self):
        self.contracts = AppendContracts().instance_list  # Вызываем метод заполнения Договоров
        self.employees = AppendEmployees().instance_list  # Вызываем метод заполнения Сотрудников
