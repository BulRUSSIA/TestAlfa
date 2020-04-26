# TODO 1)на вход подается формат вывода(консоль,файл) и любая дата(период расчета бонусов)
# TODO 2)все бонусы суммируются между собой
# TODO 3)алгоритм расчета бонусов для сотрудника
from Models.LocalData import LocalData
import datetime


def date_in(date):
    year, month, day = map(int, date.split('-'))
    full_date = datetime.date(year, month, day)

    return full_date


def main():
    date_entry = input('Введите начало периода в формате YYYY-MM-DD:')
    date_end = input('Введите конец периода в формате YYYY-MM-DD:')
    in_date = date_in(date_entry)  # период расчета бонусов
    out_date = date_in(date_end)  # период расчета бонусов
    local = LocalData()  # получаем списки сущностей при обращении к полям класса
    for employ in local.employees:  # парсим сотрудников

        print('----------------------------------------------')
        print("Фио сотрудника:", employ.employer_full_name)
        print("Бонусы сотрудника:", employ.bonus_code)
        print("Дата устройства на работу:", employ.in_work)
        print("Дата увольнения:", employ.out_work)

        if employ.out_work is not None and out_date > employ.out_work > in_date:  # Если дата увольнения попадает в
            # период расчета бонусов
            print('Бонусы не начисляются')

        """Парсим бонусы для сотрудника"""
        for bonus_id in employ.bonus_code:
            for bonus_obj in local.bonuses:
                if bonus_obj.id_ == bonus_id:
                    print("Объект бонус для конкретного сотрудника:", bonus_obj)

        """Парсим контракты для сотрудника"""
        for contract in local.contracts:
            if contract.employer_code == employ.id_:
                print("Контракт сотрудника:", contract)


if __name__ == '__main__':
    main()
