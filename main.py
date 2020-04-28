# TODO 1)на вход подается формат вывода(консоль,файл) и любая дата(период расчета бонусов)
# TODO 2)все бонусы суммируются между собой
# TODO 3)алгоритм расчета бонусов для сотрудника
from Models.LocalData import LocalData
from Logic.CalculateBonuses import Bonus_1, Bonus_2, Bonus_3, Bonus_4
import datetime
import csv

EMPLOYEES_LIST = []


class Start:
    contract = None
    id_emp = None
    max_bonus_two = 100000
    total_bonus = 0

    def date_in(self, date):
        try:
            year, month, day = map(int, date.split('-'))
            full_date = datetime.date(year, month, day)

            return full_date

        except ValueError:
            print('Не верный формат даты,введите заново!')
            self.main()

    def main(self):
        local = LocalData()  # получаем списки сущностей при обращении к полям класса
        date_entry = input('Введите начало периода в формате YYYY-MM-DD:')
        date_end = input('Введите конец периода в формате YYYY-MM-DD:')
        in_date = self.date_in(date_entry)  # период расчета бонусов
        out_date = self.date_in(date_end)  # период расчета бонусов
        for employ in local.employees:  # парсим сотрудников
            #if out_date > employ.in_work >= in_date:  # Работал ли сотрудник в заданном промежутке или былуволен
                for contract in local.contracts:  # Идем по контрактам
                    if contract.employer_code == employ.id_:  # Если в контрактах находим текущий ид сотрудника
                        self.contract = contract  # записываем контракт

                        """Парсим бонусы для сотрудника"""
                        for bonus_id in employ.bonus_code:
                            if bonus_id == 1:
                                self.total_bonus = self.total_bonus + Bonus_1(self.contract.sum_contract).bonus_sum

                            if bonus_id == 2:
                                self.total_bonus = self.total_bonus + Bonus_2(self.contract.sum_contract).bonus_sum
                                # if self.total_bonus > self.max_bonus_two:
                                #     self.total_bonus = self.max_bonus_two
                            if bonus_id == 3:
                                self.total_bonus = self.total_bonus + Bonus_3(self.contract.sum_contract,
                                                                              self.contract.data_contract,
                                                                              in_date).bonus_sum

                            if bonus_id == 4:
                                pass

                self.write_employees_bonuses(employ.id_, employ.employer_full_name)
                print(employ.employer_full_name, self.total_bonus)

    def write_employees_bonuses(self, employ_id, full_name):
        EMPLOYEES_LIST.append(
            {"код": employ_id, "ФИО": full_name, "сумма бонусов": self.total_bonus})
        with open('Отчет.csv', 'w') as f:
            writer = csv.DictWriter(
                f, fieldnames=list(EMPLOYEES_LIST[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
            writer.writeheader()
            for d in EMPLOYEES_LIST:
                writer.writerow(d)


if __name__ == '__main__':
    st = Start()
    st.main()
