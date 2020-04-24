from Models.Employee import Employee
from Models.Bonus import Bonus
from Models.Contract import Contract
from DataStructures.DataCalculationBonus import Bonuses
from DataStructures.DataContracts import Contracts
from DataStructures.DataEmployees import Employees


class AppendEmployees:
    def __init__(self):
        self.instance_list = []
        for employee in Employees:
            self.instance_employees = Employee(employee['id'], employee['employer_full_name'], employee['in_work'],
                                               employee['out_work'], employee['bonus_code'], employee['base_salary'])

            self.instance_list.append(self.instance_employees)


class AppendBonuses:
    def __init__(self):
        self.instance_list = []
        for bonus in Bonuses:
            self.instance_bonuses = Bonus(bonus['id'], bonus['bonus_percent'])

            self.instance_list.append(self.instance_bonuses)


class AppendContracts:
    def __init__(self):
        self.instance_list = []
        for contract in Contracts:
            self.instance_contracts = Contract(contract['id'], contract['employer_code'], contract['data_contract'],
                                               contract['sum_contract'])
            self.instance_list.append(self.instance_contracts)
