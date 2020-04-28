import datetime


class Bonus_1:
    """бонус 5% от суммы договоров"""

    def __init__(self, sum_bonus: int):
        PERCENT_BONUS = 5
        BONUS_CONST = float(PERCENT_BONUS / 100)
        self.bonus_sum = sum_bonus * BONUS_CONST


class Bonus_2:
    def __init__(self, sum_bonus: int):
        """бонус 10% от суммы договоров, но не более 100 000 рублей"""
        MAX_BONUS = 100000
        PERCENT_BONUS = 10
        BONUS_CONST = float(PERCENT_BONUS / 100)
        self.bonus_sum = sum_bonus * BONUS_CONST
        if self.bonus_sum > MAX_BONUS:
            self.bonus_sum = MAX_BONUS


class Bonus_3:
    """бонус 7% от суммы договоров, если сотрудник проработал в компании
более 2-х лет на дату заключения договора"""

    def __init__(self, sum_bonus: int, date_contract, date_in_employ):
        TWO_YEARS_to_DAYS = 730
        PERCENT_BONUS = 7
        BONUS_CONST = float(PERCENT_BONUS / 100)
        if date_contract - date_in_employ > datetime.timedelta(days=TWO_YEARS_to_DAYS):
            self.bonus_sum = sum_bonus * (
                    BONUS_CONST / 100)

        self.bonus_sum = 0


class Bonus_4:
    """2% оклада за каждый полный (с 1 по последний день месяца) месяц работы
в указанном периоде"""

    def __init__(self, sum_bonus: int):
        BONUS_CONST_PERCENT = float(5 / 100)
        self.bonus_sum = sum_bonus * BONUS_CONST_PERCENT
