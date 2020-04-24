from Logic.AppendDataToModel import AppendBonuses, AppendContracts, AppendEmployees


class LocalData:

    def __init__(self):
        self.bonuses = AppendBonuses()  # Вызываем метод заполнения Бонусы
        self.contracts = AppendContracts()  # Вызываем метод заполнения Договоров
        self.employees = AppendEmployees()  # Вызываем метод заполнения Сотрудников
