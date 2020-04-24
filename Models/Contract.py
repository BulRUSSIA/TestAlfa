class Contract:
    def __init__(self, id_: int, employer_code: int, data_contract, sum_contract: int):
        self.sum_contract = sum_contract
        self.data_contract = data_contract
        self.employer_code = employer_code
        self.id_ = id_
