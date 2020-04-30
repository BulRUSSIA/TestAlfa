"""Описываем модель контракты"""


class Contract:
    def __init__(self, id_: int, employee_code: int, data_contract, sum_contract: int):
        self.sum_contract = sum_contract
        self.data_contract = data_contract
        self.employee_code = employee_code
        self.id_ = id_
