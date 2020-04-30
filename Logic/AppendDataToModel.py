from Models.Employee import Employee
from Models.Contract import Contract
from DataStructures.DataContracts import Contracts
from DataStructures.DataEmployees import Employees

"""Cоздаем списки экземпляров класса Контракты и Сотрудники"""


class AppendEmployees:
    def __init__(self):
        self.instance_list = []
        for employee in Employees:
            self.instance_employees = Employee(employee['id'], employee['employee_full_name'], employee['in_work'],
                                               employee['out_work'], employee['bonus_code'], employee['base_salary'])

            self.instance_list.append(self.instance_employees)


class AppendContracts:
    def __init__(self):
        self.instance_list = []
        for contract in Contracts:
            self.instance_contracts = Contract(contract['id'], contract['employee_code'], contract['data_contract'],
                                               contract['sum_contract'])
            self.instance_list.append(self.instance_contracts)
