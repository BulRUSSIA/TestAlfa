# TODO 1)на вход подается формат вывода(консоль,файл) и любая дата(период расчета бонусов)
# TODO 2)все бонусы суммируются между собой
# TODO 3)алгоритм расчета бонусов для сотрудника
from Models.LocalData import LocalData
import datetime


class Start:
    contract = None

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

            print('----------------------------------------------')
            print("Фио сотрудника:", employ.employer_full_name)
            print("Бонусы сотрудника:", employ.bonus_code)
            print("Дата устройства на работу:", employ.in_work)
            print("Дата увольнения:", employ.out_work)

            if employ.out_work is not None and out_date > employ.out_work > in_date or employ.in_work > out_date:  # Если дата увольнения попадает в
                # период расчета бонусов
                print('Бонусы не начисляются')

            """Парсим контракты для сотрудника"""
            for contract in local.contracts:
                if contract.employer_code == employ.id_:
                    self.contract = contract
                    print("Контракт сотрудника:", self.contract)

            """Парсим бонусы для сотрудника"""
            for bonus_id in employ.bonus_code:
                for bonus_obj in local.bonuses:
                    if bonus_obj.id_ == bonus_id:
                        print("Объект бонус для конкретного сотрудника:", bonus_obj)
                        if bonus_obj.id_ == 1:
                            bonus_1 = self.contract.sum_contract * (bonus_obj.bonus_percent / 100)
                            print(self.contract.sum_contract)
                            print(bonus_1)
                        if bonus_obj.id_ == 2:
                            bonus_2 = self.contract.sum_contract * (bonus_obj.bonus_percent / 100)
                            if bonus_2 >= 100000:  # Не более ста тысяч
                                bonus_2 = 100000
                            print(self.contract.sum_contract)
                            print(bonus_2)

                        if bonus_obj.id_ == 3:
                            bonus_3 = self.contract.sum_contract * (
                                        bonus_obj.bonus_percent / 100)  # Если сотрудник проработал в компании более 2х лет
                            print(self.contract.sum_contract)
                            print(bonus_3)
                        if bonus_obj.id_ == 4:
                            bonus_4 = employ.base_salary * (bonus_obj.bonus_percent / 100)


if __name__ == '__main__':
    st = Start()
    st.main()
