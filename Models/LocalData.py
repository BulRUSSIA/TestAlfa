from Logic.AppendDataToModel import AppendBonuses, AppendContracts, AppendEmployees


class LocalData:

    def __init__(self):
        self.bonuses = AppendBonuses().instance_list  # Вызываем метод заполнения Бонусы
        self.contracts = AppendContracts().instance_list  # Вызываем метод заполнения Договоров
        self.employees = AppendEmployees().instance_list  # Вызываем метод заполнения Сотрудников
