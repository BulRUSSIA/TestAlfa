class Contract:
    def __init__(self, id_: int, employer_full_name: str, in_work, out_work, bonus_code: int, base_salary: int):
        self.base_salary = base_salary
        self.bonus_code = bonus_code
        self.out_work = out_work
        self.in_work = in_work
        self.employer_full_name = employer_full_name
        self._ = id_
