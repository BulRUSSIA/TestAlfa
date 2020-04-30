from Models.Employee import Employee
from Models.Contract import Contract
from DataStructures.DataContracts import Contracts
from DataStructures.DataEmployees import Employees

"""Cоздаем списки экземпляров класса Контракты и Сотрудники"""


class AppendEmployees:
    def __init__(self):
        self.instance_list = []
        list(map(lambda employee:
                 self.instance_list.append(
                     Employee
                     (employee['id'],
                      employee['employee_full_name'],
                      employee['in_work'],
                      employee['out_work'],
                      employee['bonus_code'],
                      employee['base_salary'])),
                 Employees))


class AppendContracts:
    def __init__(self):
        self.instance_list = []
        list(map(lambda contract:
                 self.instance_list.append(
                     Contract(contract['id'],
                              contract['employee_code'],
                              contract['data_contract'],
                              contract['sum_contract'])),
                 Contracts))
